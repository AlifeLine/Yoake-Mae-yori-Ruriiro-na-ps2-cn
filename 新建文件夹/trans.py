import glob
import os
import struct
import sys
import requests
import hashlib
import time
import json
import random
import bgi_common
import bgi_setup
import urllib.parse
import http.client
import random
import hashlib
import re
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models 
def tencentcloudtar(q):
    try:
        cred = credential.Credential("AKIDYyGRV8NYJNIxKbv5YtynKbokUFm6nQjf", "f8ct0wugJpocHlvrix8fyaSKyPceVH5z") 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-chongqing", clientProfile) 

        req = models.TextTranslateRequest()
        params = '{\"SourceText\":\"'+q+'\",\"Source\":\"ja\",\"Target\":\"zh\",\"ProjectId\":0}'
        req.from_json_string(params)
        resp = client.TextTranslate(req)
        data=json.loads(str(resp))
        print(data)
        
        print( data["TargetText"])
        return data["TargetText"]
    except Exception as e:
        return None
recompan=re.compile(">.*")
beforepan=re.compile("<.*>")
import os
rootdir = os.getcwd()  #获取当前目录
dir_jp=rootdir+"\\txt"
list_jp =os.listdir(dir_jp)
wrong=" "
for i in range(0,len(list_jp)):
    path_jp = os.path.join(dir_jp,list_jp[i])
    r=open(path_jp,"r",encoding="utf-8")
    lins=r.readlines()
    r.close()
    f=open(path_jp,"w",encoding="utf-8")
    flag=False
    textflag=False
    Exceptionflag=False
    for i in lins:
        if flag:
            if "<cnT" in i:
                if "「" in i:
                    textflag = True
                    
                text=recompan.search(i).group()
                text=text.replace(">","")
                numid=beforepan.search(i).group()
                while (True):
                    if (not Exceptionflag):
                        tmptext=text
                    text=tencentcloudtar(tmptext)
                    if text is not None:
                        Exceptionflag=False
                        break
                    else:
                        print("异常进来了")
                        Exceptionflag=True
                        time.sleep(1)
                        
                time.sleep(0.2)
                if textflag:
                    text=numid+"「"+text+"」\n"
                    textflag=False
                else:
                    text=numid+text+"\n"
                f.write(text)
                continue
            
            else:
                f.write(i)
                continue
                
            

        if "///" in i:
            flag = True
            f.write(i)
            
        else:
            f.write(i)
            
    f.close()

