import os
import json
rootdir = os.getcwd()  #获取当前目录
dir=rootdir+"\\test\\"
list =os.listdir(dir) #列出cn文件夹下所有的目录与文件
r=open("name.json",'r',encoding="utf-8")
dic=json.loads(r.read())

for i in range(0,len(list)):
    path = os.path.join(list[i])
    path_dir=dir+path
    #print (path_dir)
    f1=open (path_dir,"r",encoding="utf-8")
    text=f1.read()
    f1.close()
    f2=open(path_dir,"w",encoding="utf-8")
    for janame,cnname in dic.items():
        text=text.replace(janame,cnname)
    f2.write(text)
    f2.close()