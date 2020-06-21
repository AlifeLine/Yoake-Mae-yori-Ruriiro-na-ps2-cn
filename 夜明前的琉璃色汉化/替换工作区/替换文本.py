import os
rootdir = os.getcwd()  #获取当前目录
dir_cn=rootdir+"\cn\\"
dir_jp=rootdir+"\jp\\"
dir_source=rootdir+"\source\\"
list_cn =os.listdir(dir_cn) #列出cn文件夹下所有的目录与文件
wrong=""
success=""
list_source =os.listdir(dir_source)
for i in range(0,len(list_source)):
    path_source = os.path.join(list_source[i])
    path_cnt = dir_cn+path_source
    path_scrip=dir_source+path_source
    #if os.path.exists(path_cnt):
    for i1 in range(0,len(list_cn)):#遍历cn文件，保证脚本全部翻译
        path_file = os.path.join(list_cn[i1])
        path_jp = dir_jp+path_file
        path_cn = dir_cn+path_file
        command="python replace.py " + path_scrip
        command1=command+" "+path_jp
        command_fal=command1+" "+path_cn
        #print(command_fal)
        os.system(command_fal)
    success+=path_source
    success+="\n"
    #else:
        #wrong+=path_source
        #wrong+="\n"
        #continue
    #print(path_cn)
print("\n")    
#print("错误的文件：\n",wrong)
print("成功的文件：\n",success,)