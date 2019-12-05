#coding=utf-8


def set_func(param):
    def call_func(*args,**kwargs):
        levle = args[0]
        if levle == 1:
            print("权限级别1")
        elif levle == 2:
            print("权限级别2")
        return param()
    return call_func

@set_func
def test1():
     print("---test1---")
     return "ok"

@set_func
def test2():
    print("---test2---")
    return "ok2"



#这个权限验证的级别方式不可取，不能又函数调用方来确定自己的验证级别；还有如果在调用函数处加参数，如果调用装饰器的函数量很大，会导致工作量太大
test1(1)

test2(2)

