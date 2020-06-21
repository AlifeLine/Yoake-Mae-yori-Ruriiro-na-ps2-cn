
#/usr/bin/env python
#coding=utf8
import urllib.parse
import http.client
import random
import hashlib
import time
 
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
        #print(s)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return s
with open("整合jp.txt","r",encoding="utf-8")as jp,open("整合cn.txt","a",encoding="utf-8") as cn :
    for lines in jp:
        tran_line=youdaoTranslate(lines)
        cn.write(tran_line[0])
        cn.write("\n")
        #time.sleep( 0.3 )




