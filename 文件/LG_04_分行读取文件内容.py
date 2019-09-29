#coding=utf-8

file = open("readme")


while True:
    text = file.readline()
    #如果读取不到，就退出
    if not text:
        break

    #没读取一行的末尾已经有了一个'\n'
    print(text,end="")

file.close()