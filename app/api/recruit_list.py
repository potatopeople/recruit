from threading import Thread
import json
import time
from app.http.Spider import Spider
from app.city_data import anchors as city


def postHttp(start, end):
    anchor = []
    for item in city[start:end]:
        go = Spider()
        num = item['value']
        i = 1
        while True:
            time.sleep(0.5)
            data = go.run(
                    'https://search.51job.com/list/' + str(num) + ',000000,0000,00,9,99,"%2520",2,' + str(
                            i) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            )
            if not data:
                print(item['name'], '*'*15, '爬取完成。')
                go.prompt = ''
                file = open('./app/data/' + item['name'] + '.json', 'w')
                file.write(json.dumps(anchor if len(anchor) else '此地暂无数据'))
                file.flush()
                file.close()
                anchor = []
                break
            else:
                for items in data:
                    anchor.append(items)
                print(item['name'], '  第***', i, '***页')
                i += 1

def run():
    one = Thread(args=(0, 60), target=postHttp)
    two = Thread(args=(60, 120), target=postHttp)
    three = Thread(args=(120, 180), target=postHttp)
    four = Thread(args=(180, 240), target=postHttp)
    five = Thread(args=(240, 300), target=postHttp)
    six = Thread(args=(300, 360), target=postHttp)
    seven = Thread(args=(360, 375), target=postHttp)
    eight = Thread(args=(375, 390), target=postHttp)
    nine = Thread(args=(390, 405), target=postHttp)
    ten = Thread(args=(405, 411), target=postHttp)
    one.start()
    two.start()
    three.start()
    four.start()
    five.start()
    six.start()
    seven.start()
    eight.start()
    nine.start()
    ten.start()
    one.join()
    two.join()
    three.join()
    four.join()
    five.join()
    six.join()
    seven.join()
    eight.join()
    nine.join()
    ten.join()
