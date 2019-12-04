#coding=utf-8

def set_fun(para):
    print("---开始执行装饰---")
    def set_fun_in(a):
        print("这是内函数---")
        para(a)
    return set_fun_in

@set_fun
def test1(num):
    print("这是参数---%d" % num)


@set_fun
def test2(num):
    print("这是参数---%d" % num)

#
# test1(100)
# test2(200)