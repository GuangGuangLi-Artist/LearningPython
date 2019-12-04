#coding=utf-8



def func(param):
    def func_1():
        print("--这是验证机制1")
        print("--这是验证机制2")
        param()
    return func_1

@func  #等价于test = func(test)   test()
def test():
    print("这是test1")


test()