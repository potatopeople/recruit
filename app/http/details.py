import time
import requests
import re

class Details:

    data = []
    header = {
        'Cookie': 'guid=7283bf0d46dc320d6bc03d5da547dd06; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; slife=lastvisit%3D010000%26%7C%26; adv=adsnew%3D1%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fsp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fDewkY0XJVb00uiAsK-iKdI000002SLnNC00000BtSW6c.THLZ_Q5n1VeHksK85HRLnjc3nW6kgv99UdqsusK15ymkny7-PHfLnj0snhmLnj60IHdawbFjnYnznWIjnWTdfYPKf1TdfHI7wWTzrRFKnYDLnfK95gTqFhdWpyfqn1cdrjc4nHcLPzusThqbpyfqnHm0uHdCIZwsT1CEQLwzmyP-QWRkphqBQhPEUiqYTh7Wui4spZ0Omyw1UMNV5HnkPW64P16hmyGs5y7cRWKWiDYvHZb4IAD1RgNrNDukmWFFINbzrgwnndF8HjPrUAFHrgI-Uj94HRw7PDkVpjKBNLTEyh42IhFRny-uNvkou79aPBuo5HnvuH0dPA79njfdrynzuywbPycYPvmdPvPBPWDsuj6z0APzm1YdnHTdr0%2526tpl%253Dtpl_11534_19968_16032%2526l%253D1513207727%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526xp%25253Did%2528%25252522m3258291277_canvas%25252522%2529%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D248%2526ie%253Dutf-8%2526f%253D8%2526srcqid%253D3260661630431035150%2526tn%253D57028281_hao_pg%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526oq%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526rqlang%253Dcn%2526sc%253DUWYdP10zrjc3nNqCmyqxTAThIjYkPHmznW0snHfvnjTzFhnqpA7EnHc1Fh7W5HDYnHmLrjRknH6%2526ssl_sample%253Dnormal%2526H123Tmp%253Dnunew7%26%7C%26adsnum%3D3168978; search=jobarea%7E%60091800%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA091800%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562204949%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562034881%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA080700%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562047809%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA080700%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%CA%D0%B3%A1%D7%A8%D4%B1%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562047927%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA070000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562035386%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21',
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 73.0.3683.86Safari / 537.36'
    }
    reg_details = '<p class="msg ltype" title=.*?>(.*?)</p>'

    def __details_html(self, data):  # 职位详情页面
        for item in data:
            time.sleep(0.5)
            while True:
                try:
                    details = requests.get(
                        url='https://jobs.51job.com/jiaxing/' + item['id'] + '.html',
                        params={
                            's': '01',
                            't': '0'
                        },
                        headers=self.header
                    )
                    if details.status_code == 200:
                        print(item['name'], '*'*10, item['id'])
                        details.encoding = 'gbk'
                        self.__refine_details(details.text)
                        break
                    else:
                        print(item['name'], '*'*10, item['id'], '请求错误')
                except Exception as e:
                    print('发生错误：', e)
        print('结束', '*'*20)
        for item in self.data:
            print(item)
        #return anchor

    def __refine_details(self, html):  # 详情数据匹配
        data = re.findall(self.reg_details, html, re.S)
        data = re.sub('&nbsp;|[\d-]{5}发布|招|\\t', '', data[0], 0, re.S)
        data = re.findall('</span>(.*?)<span>|</span>([\w\s]*)', data, re.S)
        for item in data:
            if item[0] + item[1] == '':
                data.remove(item)
        self.data.append(data)

    def __run(self):
        pass