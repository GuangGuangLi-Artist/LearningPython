#coding=utf-8


#打开文件
file_read = open("readme")
file_write = open("readme附件","w")



#读、写文件
while True:
    text = file_read.readline()

    if not text:
        print("success")
        break

    file_write.write(text)



#关闭文件
file_read.close()
file_write.close()