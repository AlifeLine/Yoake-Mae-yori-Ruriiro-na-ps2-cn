import requests
import hashlib
import time
import json
import random


class Youdao(object):
    def __init__(self, msg):
        self.msg = msg.encode('utf-8')
        self.url = 'https://fanyi.qq.com/api/translate'

    def get_result(self):
        '''headers里面有一些参数是必须的，注释掉的可以不用带上'''
        uuid = int(time.time() * 1000)
        data = {
                    "source":"auto",
                    "target":"zh",
                    "sourceText":self.msg,
                    "qtv":"1855bd2285bf7cab",
                    "qtk":"i5woJXkx08mO5ewt0UzbAcXesHk3OdoyoPvu4olpRGGBO49pdNE1g1a6y1mRhR9oSUKo0vzdNlKRXMzruP4477pudON6Rmjloe7IlV3+LmpBJfCrSG7bIUOlphAglDpCW2TsCJgpto5onEWjkXdqBA==",
                    "sessionUuid":"translate_uuid" + str(uuid)
        }
        headers = {
         "Accept": "application/json, text/javascript, */*; q=0.01",
         "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "fanyi.qq.com",
        "Origin": "https://fanyi.qq.com",
        "Referer": "https://fanyi.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        # 请求体的长度
        "Content-Length": str(len(str(data))),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "fy_guid=60a69569-d3b4-47bf-bf69-6b713c2d86d4; gr_user_id=c14793de-a4d9-45d0-9d17-1b69dfa6687d; grwng_uid=245abc96-00b3-4cc5-95a4-4c91631481c5; 8507d3409e6fad23_gr_session_id=e3605331-a131-4137-999f-de9b01a6b2e2; 8507d3409e6fad23_gr_session_id_e3605331-a131-4137-999f-de9b01a6b2e2=true; qtv=1855bd2285bf7cab; qtk=i5woJXkx08mO5ewt0UzbAcXesHk3OdoyoPvu4olpRGGBO49pdNE1g1a6y1mRhR9oSUKo0vzdNlKRXMzruP4477pudON6Rmjloe7IlV3+LmpBJfCrSG7bIUOlphAglDpCW2TsCJgpto5onEWjkXdqBA==; openCount=20"
        }
        html = requests.post(self.url, data=data, headers=headers).text
        print(html)

        infos = json.loads(html)
        result = infos['translate']['records'][0]['targetText']
        print(result)
        return result
                
if __name__ == '__main__':
    y = Youdao('身だしなみを整えておるようなので、しばらくお待ち頂けますか？')
    y.get_result()