#coding=utf-8


num = 10

def demo1():

    #不允许直接修改全局变量的值
    num = 99
    print("demo1 ==>%d" % (num))


def demo2():

    print("demo2 ==>%d" % (num))


demo1()
demo2()