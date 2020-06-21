import os
rootdir = os.getcwd()  #获取当前目录
dir=rootdir+"\已校对\\"
list =os.listdir(dir) #列出cn文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(list[i])
    path_bak=path+".bak"
    path_dir=dir+path
    path_bak_dir=dir+path_bak
    #print (path_dir)
    with open (path_dir,"r",encoding="utf-8") as f1,open(path_bak_dir,"a",encoding="utf-8") as f2:
        for line in f1:
            if "フィーナ" in line:
                line=line.replace("フィーナ","菲娜")
                f2.write(line)
            elif "左門" in line:
                line=line.replace("左門","左门")
                f2.write(line)
            elif "ミア" in line:
                line=line.replace("ミア","米娅")
                f2.write(line)
            elif "達哉" in line:
                line=line.replace("達哉","达哉")
                f2.write(line)
            elif "さやか" in line:
                line=line.replace("さやか","沙耶香")
                f2.write(line)
            elif "フィアッカ" in line:
                line=line.replace("フィアッカ","菲娅卡")
                f2.write(line)
            elif "ペペロンチーノ" in line:
                line=line.replace("ペペロンチーノ","贝贝隆奇那")
                f2.write(line)
            elif "カルボナーラ" in line:
                line=line.replace("カルボナーラ","卡尔伯纳拉")
                f2.write(line)
            elif "綺麗な女の子" in line:
                line=line.replace("綺麗な女の子","漂亮的女孩子")
                f2.write(line)
            elif "エステル" in line:
                line=line.replace("エステル","艾斯蒂尔")
                f2.write(line)
            elif "アラビアータ" in line:
                line=line.replace("アラビアータ","阿拉比特")
                f2.write(line)
            elif "イタリアンズ" in line:
                line=line.replace("イタリアンズ","意大利一族")
                f2.write(line)
            elif "モーリッツ" in line:
                line=line.replace("モーリッツ","莫里斯")
                f2.write(line)
            elif "女の子" in line:
                line=line.replace("女の子","女孩子")
                f2.write(line)
            elif "リース" in line:
                line=line.replace("リース","莉斯")
                f2.write(line)
            elif "八百屋のオヤジ" in line:
                line=line.replace("八百屋のオヤジ","蔬菜店的大叔")
                f2.write(line)
            elif "魚屋のおばさん" in line:
                line=line.replace("魚屋のおばさん","卖鱼的阿姨")
                f2.write(line)
            elif "配布お姉さん" in line:
                line=line.replace("配布お姉さん","发传单的姐姐")
                f2.write(line)
            elif "クラスメート" in line:
                line=line.replace("クラスメート","同班同学")
                f2.write(line)
            elif "黒服" in line:
                line=line.replace("黒服","黑衣人")
                f2.write(line)
            elif "カレン" in line:
                line=line.replace("カレン","卡莲")
                f2.write(line)
            elif "おばさん" in line:
                line=line.replace("おばさん","大妈")
                f2.write(line)
            elif "ライオネス国王" in line:
                line=line.replace("ライオネス国王","莱昂内斯国王")
                f2.write(line)
            elif "en" in line:
                line=line.replace("en","cn")
                f2.write(line)
            else:
                f2.write(line)
                continue