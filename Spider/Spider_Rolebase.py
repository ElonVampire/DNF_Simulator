from __future__ import unicode_literals
from lxml import etree
import requests, queue, csv, datetime, re, random, time, json, os
from threading import Thread
from psycopg2 import *

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
]

header = {
    "Host": "tools-api.colg.cn",
    "Origin": "http://tools.colg.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}


# params = {
#     'id': 119,
#     'pos_id': 2,
#     'roleId': 21,
#     'version': 0
# }

def getimage(path):
    header2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

    r = requests.get(f"http://tools.colg.cn{path}", headers=header2)
    with open(path[1:], 'wb') as f:
        f.write(r.content)


def getbase(roleid):
    params = {
        'id': roleid,
    }
    if not os.path.exists(f'Base/{roleid}.json'):
        response = requests.post(
            'http://tools-api.colg.cn/api/v1/profession/info?token=MTU0ODU4NTE4Nn-gkpmzrtuuf3t4z5WroZO80KTVwniljciIeIe8jsBpi6B72b6XzGiKoXTPlauhk7Ddn6M',
            headers=header,
            params=params)
        print(response.text)
        with open(f'Base/{roleid}.json', 'w', encoding='utf8') as f:
            jsdata = json.loads(response.text.encode('utf8'))
            a = json.dumps(jsdata, ensure_ascii=False)
            f.write(a)
        try:
            path = jsdata['data']['picture']
            pathdir = os.path.dirname(path[1:])
            if not os.path.exists(pathdir):
                os.mkdir(pathdir)
            if not os.path.exists(path[1:]):
                getimage(path)
        except:
            pass
        print(f'{roleid}已完成')
        time.sleep(3)


def getinfo(id, pid, roleid):
    params = {
        'id': id,
        'pos_id': pid,
        'roleId': roleid,
        'version': 0
    }
    response = requests.post(
        'http://tools-api.colg.cn/api/v1/equip/info?token=MTU0Nzk3ODM3NH-gkpmzrtuuf3t4lI2spZO80KzgsobSZ7eIdIW5ppdoi6CD2MrU0GiKoXyUjaylk8bNn6M',
        headers=header,
        params=params)
    jsdata = json.loads(response.text.encode('utf8'))
    index = jsdata['data']['equip']['equipment_index']
    with open(f'Equipments/{index}.json', 'w', encoding='utf8') as f:
        a = json.dumps(jsdata, ensure_ascii=False)
        f.write(a)


if __name__ == '__main__':
    str = '{"code":"1","msg":"","data":[{"pro_id":1,"name":"\u9b3c\u5251\u58eb\uff08\u7537\uff09","pros":[{"trans_id":6,"transfer_name":"\u963f\u4fee\u7f57"},{"trans_id":16,"transfer_name":"\u72c2\u6218\u58eb"},{"trans_id":42,"transfer_name":"\u9b3c\u6ce3"},{"trans_id":43,"transfer_name":"\u5251\u9b42"}]},{"pro_id":2,"name":"\u9b3c\u5251\u58eb\uff08\u5973\uff09","pros":[{"trans_id":2,"transfer_name":"\u6697\u6bbf\u9a91\u58eb"},{"trans_id":4,"transfer_name":"\u6d41\u6d6a\u6b66\u58eb"},{"trans_id":15,"transfer_name":"\u5951\u9b54\u8005"},{"trans_id":34,"transfer_name":"\u9a6d\u5251\u58eb"}]},{"pro_id":3,"name":"\u795e\u67aa\u624b \uff08\u7537\uff09","pros":[{"trans_id":1,"transfer_name":"\u5f39\u836f\u4e13\u5bb6(\u7537)"},{"trans_id":19,"transfer_name":"\u67aa\u70ae\u5e08(\u7537)"},{"trans_id":22,"transfer_name":"\u6f2b\u6e38\u67aa\u624b(\u7537)"},{"trans_id":37,"transfer_name":"\u673a\u68b0\u5e08(\u7537)"}]},{"pro_id":4,"name":"\u795e\u67aa\u624b \uff08\u5973\uff09","pros":[{"trans_id":18,"transfer_name":"\u673a\u68b0\u5e08(\u5973)"},{"trans_id":28,"transfer_name":"\u6f2b\u6e38\u67aa\u624b(\u5973)"},{"trans_id":30,"transfer_name":"\u5f39\u836f\u4e13\u5bb6(\u5973)"},{"trans_id":36,"transfer_name":"\u67aa\u70ae\u5e08(\u5973)"}]},{"pro_id":5,"name":"\u9b54\u6cd5\u5e08\uff08\u7537\uff09","pros":[{"trans_id":5,"transfer_name":"\u51b0\u7ed3\u5e08"},{"trans_id":8,"transfer_name":"\u9010\u98ce\u8005"},{"trans_id":13,"transfer_name":"\u8840\u6cd5\u5e08"},{"trans_id":14,"transfer_name":"\u5143\u7d20\u7206\u7834\u5e08"},{"trans_id":25,"transfer_name":"\u6b21\u5143\u884c\u8005"}]},{"pro_id":6,"name":"\u9b54\u6cd5\u5e08\uff08\u5973\uff09","pros":[{"trans_id":3,"transfer_name":"\u6218\u6597\u6cd5\u5e08"},{"trans_id":38,"transfer_name":"\u9b54\u9053\u5b66\u8005"},{"trans_id":39,"transfer_name":"\u5143\u7d20\u5e08"}]},{"pro_id":7,"name":"\u5b88\u62a4\u8005","pros":[{"trans_id":40,"transfer_name":"\u5e15\u62c9\u4e01"},{"trans_id":41,"transfer_name":"\u9f99\u9a91\u58eb"},{"trans_id":46,"transfer_name":"\u7cbe\u7075\u9a91\u58eb"}]},{"pro_id":8,"name":"\u683c\u6597\u5bb6\uff08\u7537\uff09","pros":[{"trans_id":9,"transfer_name":"\u6c14\u529f\u5e08(\u7537)"},{"trans_id":24,"transfer_name":"\u6563\u6253(\u7537)"},{"trans_id":33,"transfer_name":"\u67d4\u9053\u5bb6(\u7537)"}]},{"pro_id":9,"name":"\u683c\u6597\u5bb6\uff08\u5973\uff09","pros":[{"trans_id":12,"transfer_name":"\u6563\u6253(\u5973)"},{"trans_id":17,"transfer_name":"\u6c14\u529f\u5e08(\u5973)"},{"trans_id":32,"transfer_name":"\u67d4\u9053\u5bb6(\u5973)"}]},{"pro_id":10,"name":"\u5723\u804c\u8005\uff08\u7537\uff09","pros":[{"trans_id":20,"transfer_name":"\u9a71\u9b54\u5e08"},{"trans_id":23,"transfer_name":"\u5723\u9a91\u58eb(\u7537)"},{"trans_id":31,"transfer_name":"\u84dd\u62f3\u5723\u4f7f"},{"trans_id":35,"transfer_name":"\u590d\u4ec7\u8005"}]},{"pro_id":11,"name":"\u5723\u804c\u8005\uff08\u5973\uff09","pros":[{"trans_id":7,"transfer_name":"\u5723\u9a91\u58eb(\u5973)"},{"trans_id":10,"transfer_name":"\u5deb\u5973"},{"trans_id":11,"transfer_name":"\u5f02\u7aef\u5ba1\u5224\u8005"},{"trans_id":27,"transfer_name":"\u8bf1\u9b54\u8005"}]},{"pro_id":12,"name":"\u6697\u591c\u4f7f\u8005","pros":[{"trans_id":21,"transfer_name":"\u5f71\u821e\u8005"},{"trans_id":26,"transfer_name":"\u523a\u5ba2"},{"trans_id":45,"transfer_name":"\u6b7b\u7075\u672f\u58eb"}]},{"pro_id":13,"name":"\u67aa\u5251\u58eb","pros":[]},{"pro_id":14,"name":"\u9b54\u67aa\u58eb","pros":[{"trans_id":29,"transfer_name":"\u5f81\u6218\u8005"},{"trans_id":44,"transfer_name":"\u51b3\u6218\u8005"},{"trans_id":54,"transfer_name":"\u72e9\u730e\u8005"},{"trans_id":55,"transfer_name":"\u6697\u67aa\u58eb"}]},{"pro_id":99,"name":"\u9ed1\u6697\u6b66\u58eb","pros":[]},{"pro_id":100,"name":"\u7f14\u9020\u8005","pros":[]}]}'
    jsondata = json.loads(str)
    with open('baseError.txt', 'w', encoding='utf8') as g:
        for i in jsondata['data']:
            for j in i['pros']:
                if not os.path.exists(f'Equip/{j["transfer_name"]}'):
                    os.mkdir(f'Equip/{j["transfer_name"]}')
                try:
                    getbase(j['trans_id'])
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    g.write(f"{j['transfer_name']}\n")
                    time.sleep(1000)
