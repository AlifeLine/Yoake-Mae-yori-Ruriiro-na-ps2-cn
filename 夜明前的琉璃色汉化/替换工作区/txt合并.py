import os
rootdir = os.getcwd()  #获取当前目录
dir_source=rootdir+"\\远山剧本\\"
wrong=""
success=""
list_source =os.listdir(dir_source)
for i in range(0,len(list_source)):
    path_source = os.path.join(dir_source,list_source[i])
    with open(path_source, "r", encoding="utf-8") as f1,open("远山剧本整合.txt", "a", encoding="utf-8") as f2:
        f2.write(f1.read())
        #f2.write("\n")
        f2.write("+++++++++++++++++++++++++++++++++=+++++++=++++++++++++=+++++=+++=+++\n")