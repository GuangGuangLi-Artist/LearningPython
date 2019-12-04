#coding=utf-8

def func(param):
    def func_1():
        print("--这是验证机制1")
        print("--这是验证机制2")
        #param
        """
        --这是验证机制1
        --这是验证机制2
        """
        param()
        """
        --这是验证机制1
        --这是验证机制2
        这是test1
        """
    return func_1



@func
def test():
    print("这是test1")

test()