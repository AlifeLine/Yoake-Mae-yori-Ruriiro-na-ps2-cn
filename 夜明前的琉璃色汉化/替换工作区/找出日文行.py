import os
import requests
import hashlib
import time
import json
import random



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

rootdir = os.getcwd()  #获取当前目录
dir_source=rootdir+"\\名字以翻译\\"
jp_line=""
success=""
jp_list=[]

list_source =os.listdir(dir_source)
with open("日文字符.txt", "r", encoding="utf-8") as f2:
    for lines in f2:
        jp_list.append(lines)
len_list=len(jp_list)
for i in range(0,len(list_source)):
    path_source = os.path.join(dir_source,list_source[i])
    with open(path_source, "r", encoding="utf-8") as f1:
        n=0
        for line in f1:
            n=n+1
            if "ja"in line:
                continue 
            else:

                for i in range(len_list):
                    if jp_list[i] in line:
                        if n<40:
                            continue
                        else:
                            jp_line+=path_source
                            jp_line+="\n"
                            jp_line+="行数为"
                            jp_line+=str(n)
                            jp_line+="\n"
                            tran_jp=youdaoTranslate(line)
                            jp_line+="日文："
                            jp_line+=line
                            jp_line+="翻译为："+tran_jp[0]+"\n"

                    else:
                        continue
print(jp_line)
with open("tran_jp.txt","w",encoding="utf-8") as f3:
    f3.write(jp_line)
            

