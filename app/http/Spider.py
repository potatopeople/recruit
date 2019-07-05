import requests
import re
import pymysql
import setting as config


class Spider:

    data = []
    url = ''
    city = ''
    value = ''
    reg = '<div class="el">(.*?)</div>'
    reg_id = '<input class="checkbox" .*? value="(.*?)" .*?>'
    reg_city = '<div .*? id="work_position_click">.*?<input .*? value="(.*?)">.*?</div>'
    reg_name = '<span>.*?<a target="_blank" title="(.*?)" .*>.*?</span>'
    reg_company = '<span class="t2"><a target="_blank" title="(.*?)" .*></span>'
    reg_address = '<span class="t3">(.*?)</span>'
    reg_wages = '<span class="t4">(.*?)</span>'
    reg_release = '<span class="t5">(.*?)</span>'

    def __read_html(self):
        while True:
            try:
                html = requests.get(url=self.url)
                html.encoding = 'gbk'
                if html.status_code == 200:
                    return html.text
                else:
                    print('错误：', requests.RequestException)
            except Exception as e:
                print('请求错误', e)

    def __reg_html(self, html):  # 匹配数据
        node = re.findall(self.reg, html, re.S)
        anchor = []
        if node:
            for item in node:
                id = re.findall(self.reg_id, item, re.S)
                name = re.findall(self.reg_name, item, re.S)
                company = re.findall(self.reg_company, item, re.S)
                address = re.findall(self.reg_address, item, re.S)
                wages = re.findall(self.reg_wages, item, re.S)
                release = re.findall(self.reg_release, item, re.S)
                anchor.append(
                    {
                        'id': id,
                        'name': name,
                        'company': company,
                        'address': address,
                        'wages': wages,
                        'release': release
                    }
                )
            return anchor
        else:
            return False

    @staticmethod
    def __refine_data(data):  # 过滤数据
        anchor = lambda data: {
            'id': data['id'][0].strip() if len(data['id']) else '',
            'name': data['name'][0].strip() if len(data['name']) else '暂无详细信息',
            'company': data['company'][0].strip() if len(data['company']) else '暂无详细信息',
            'address': data['address'][0].strip() if len(data['address']) else '暂无详细信息',
            'wages': data['wages'][0].strip() if len(data['wages']) >= 1 else '暂无详细信息',
            'release': data['release'][0].strip() if len(data['release']) else '暂无详细信息'
        }
        data = map(anchor, data)
        return list(data)

    @staticmethod
    def __save_data(data):
        anchor = []
        for item in data:
            anchor.append(
                (item['name'], item['company'], item['address'], item['wages'], item['release'], item['id'])
            )
        db = pymysql.connect(
            host=config.HOST, user='root',
            password=config.PASSWORD, database=config.DATABASE
        )
        cursor = db.cursor()  # 建立游标
        sql = 'insert into introduction(name,company,address,wages,reData,value) values (%s,%s,%s,%s,%s,%s)'
        try:
            cursor.executemany(sql, anchor)
            db.commit()
        except Exception as e:
            print('电影提交失败：', e)
            db.rollback()
            # print('开始拆分提交')
            # for item in anchor:
            #     try:
            #         cursor.execute(sql, item)
            #         db.commit()
            #     except Exception as e:
            #         print(e)
            #         db.rollback()
            #     finally:
            #         cursor.close()
            #         db.close()

    def run(self, url):
        self.url = url
        html = self.__read_html()
        if html:
            data = self.__reg_html(html)
            if data:
                data = self.__refine_data(data)
                self.__save_data(data)
                return data
            else:
                return False
        else:
            return False
