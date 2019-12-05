#coding=utf-8


def set_fun(para):
    def set_fun_in(*args,**kwargs):
        print("这是内函数---")
        para(*args,**kwargs)#拆包
    return set_fun_in

@set_fun
def test1(num,*args,**kwargs):
    print("这是参数---%d" % num)
    print("这是参数---",args)
    print("这是参数---",kwargs)

test1(100)
test1(100,200)
test1(100,200,300,mm=120)