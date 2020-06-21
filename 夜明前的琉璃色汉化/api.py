#/usr/bin/env python
#coding=utf8
import urllib.parse
import http.client
import random
import hashlib
 
appKey = '31fd3dcadab304f8'
secretKey = 'AO5xKNJK878ttikdrCDtnc411EfoqVrX'
 
def youdaoTranslate(q):
    httpClient = None
    myurl = '/api'
    fromLang = 'ja'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)
    sign = appKey+q+str(salt)+secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl+'?appKey='+appKey+'&q='+ urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        s = eval(response.read().decode("utf-8"))['translation']
        print(s)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return s
 
if __name__ == '__main__':
    ss = youdaoTranslate('大丈夫')
    print(ss)