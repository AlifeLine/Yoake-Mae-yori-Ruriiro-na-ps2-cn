#!/usr/bin/env python3

# BGI script inserter

import glob
import os
import re
import struct
import sys

def get_text(path):
	for line in open(path,"r",encoding="utf-8",errors="ignore"): 
		line = line.rstrip('\n')
		print (line)
		return line
			
def alter(file,old_str,new_str):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)





def get_alltext(path,readlineflag=False):
    with open(path,"r",encoding="utf-8") as f:
        if readlineflag:
            text = f.readlines()
        else:
            text = f.read()
    return text

"""
    :param filepath_1: 1.txt文件路径
    :param filepath_ja: 日文.txt文件路径
    :param filepath_cn: 中文.txt文件路径
    :param testflag: 开启 结果写在test.txt文件下，不开启则覆盖1.txt文件
    :return: None
"""
def just_alter(filepath_1,filepath_ja,filepath_cn, testflag = False):
    result_1 =get_alltext(filepath_1)
    result_ja =get_alltext(filepath_ja,True)
    result_cn =get_alltext(filepath_cn,True)
    len_cn = len(result_cn)
    len_ja = len(result_ja)
    for i in range(min(len_cn,len_ja)):
        item_ja = result_ja[i].rstrip("\n")
        item_cn = result_cn[i].rstrip("\n")
        try:
            result_1 = result_1.replace(item_ja, item_cn,2)
            #print(f'{item_ja}  {item_cn}')
            #print(result_1.replace(item_ja, item_cn))

        except Exception as e:
            pass
            #print(f"出现了错误 {e}")
    #直接覆盖写
    if testflag:
        newfilepath = "./test.txt"
    else:
        newfilepath = filepath_1
    with open(newfilepath,"w",encoding="utf-8") as f:
        f.write(result_1)
    #print(result_1)


if __name__ == '__main__':
    path_1 =  sys.argv[1]
    path_ja = sys.argv[2]
    path_cn = sys.argv[3]
    
    just_alter(path_1,path_ja,path_cn,False)
