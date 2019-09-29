#coding=utf-8

#打开文件
file = open("readme")



#读取文件

text = file.read()

print(text)
print(len(text))
print("*" * 50)

#read方法执行结束后，文件指针会移动到末尾，下次调用时就不能读取文件内容了
text = file.read()
print(text)
print(len(text))


#关闭文件

file.close()