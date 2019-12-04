#coding=utf-8


x = 300
def test1():
    x = 200
    def test2():
        nonlocal x    #闭包修改数据时需要加nonlocal
        print("----1---%s" % x)
        x = 100
        print("----2---%s" % x)
    return test2


t1 = test1()
t1()

"""
运行结果
----1---200
----2---100
"""
