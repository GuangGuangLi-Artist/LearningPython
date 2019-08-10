#coding=utf-8

#在函数内部定义的变量，其他位置不能使用

def demo1():

    num = 10

    print("在函数内部定义的变量是%d" %(num))



def demo2():

    print("%d" %(num))


demo1()
demo2()


#在函数外面引用变量num
#print("函数内部的变量是%d" %(num))NameError: name 'num' is not defined
