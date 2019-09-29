#coding=utf-8


#打开文件
file = open("readme","a",encoding="utf-8")

#写入内容
file.write("/写入新内容/以a（追加）方式写入")


#关闭文件
file.close()