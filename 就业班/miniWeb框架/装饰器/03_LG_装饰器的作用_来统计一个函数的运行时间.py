#coding=utf-8

import time



def func(param):
    def func_1():
        start_time = time.time()
        param()
        stop_time = time.time()
        all_time = (stop_time - start_time)
        print("函数的运行时间是%f" % all_time)
    return func_1

@func
def test():
    for i in range(10000000):
        pass


test()