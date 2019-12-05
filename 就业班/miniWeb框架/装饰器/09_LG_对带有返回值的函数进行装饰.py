#coding=utf-8


def set_fun(para):
    def set_fun_in(*args,**kwargs):
        print("这是内函数---")
        return para(*args,**kwargs)#<----在这里接收函数的返回值
    return set_fun_in

@set_fun
def test1(num,*args,**kwargs):
    print("这是参数---%d" % num)
    print("这是参数---",args)
    print("这是参数---",kwargs)
    return "ok"
    return "ok1"


@set_fun
def test2(num):
    pass

ret = test1(100)
print(ret)


ret = test2(100)
print(ret)

