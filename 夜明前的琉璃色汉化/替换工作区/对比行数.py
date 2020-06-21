import os
rootdir = os.getcwd()  #获取当前目录
dir_cn=rootdir+"\cn"
dir_jp=rootdir+"\jp"
list_cn =os.listdir(dir_cn) #列出文件夹下所有的目录与文件
list_jp =os.listdir(dir_jp)
wrong=" "
for i in range(0,len(list_cn)):
    path_cn = os.path.join(dir_cn,list_cn[i])
    path_jp = os.path.join(dir_jp,list_jp[i])
    count_cn = len(open(path_cn, 'r',encoding="utf-8").readlines())
    count_jp = len(open(path_jp, 'r',encoding="utf-8").readlines())
    if count_cn!=count_jp:
        wrong+=path_cn
        wrong+="\n"
    else:
        continue
    #print(path_cn)
print("\n")    
print("有这些文件错误：\n",wrong)
    