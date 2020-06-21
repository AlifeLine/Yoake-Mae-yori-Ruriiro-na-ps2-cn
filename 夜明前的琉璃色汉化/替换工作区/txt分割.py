import os
rootdir = os.getcwd()  #获取当前目录
dir_source=rootdir+"\source\\"
wrong=""
success=""
n=0
file="yak10010.txt"
list_source =os.listdir(dir_source)
for i in range(0,len(list_source)):
    path_source = os.path.join(list_source[i])
    #if os.path.exists(path_cnt):
    with open("远山剧本整合.txt", "r", encoding="utf-8") as f1:

        for lines in f1:
            piece=lines
            file=list_source[n]
            if "+++++++++++++++++++++++++++++++++=+++++++=++++++++++++=+++++=+++=+++" in lines:
                n=n+1
            else:
                with open(file,'a',encoding="utf-8")as f2:
                    f2.write(lines)
