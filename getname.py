import glob
import os
import struct
import sys
import requests
import hashlib
import time
import json
import random
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
recompan=re.compile(">.*")
import os
rootdir = os.getcwd()  #获取当前目录
dir_jp=rootdir+"\\txt"
list_jp =os.listdir(dir_jp)
diclist={}
f=open("name.json","w",encoding="utf-8")
for i in range(0,len(list_jp)):
    path_jp = os.path.join(dir_jp,list_jp[i])
    r=open(path_jp,"r",encoding="utf-8")
    lins=r.readlines()
    r.close()
    for i in lins:
        if "<jaN" in i:
            text=recompan.search(i).group()
            text=text.replace(">","")
            if text not in diclist:
                tartext=tencentcloudtar(text)
                diclist[text]=tartext
            time.sleep(0.2)

            continue
            
  
f.write(json.dumps(diclist))
f.close()

