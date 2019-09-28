#coding=utf-8

def demo1():

    num = int(input("请输入一个整数"))
    return num


def demo2():

    return demo1()

#利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)
