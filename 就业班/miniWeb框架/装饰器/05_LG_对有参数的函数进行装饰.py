#coding=utf-8

def set_fun(para):
    def set_fun_in(a):#<<<-----num的形参
        print("这是内函数---")
        para(a)#<<<-----num的形参
    return set_fun_in

@set_fun
def test(num):#<<<-----形参num
    print("这是参数---%d" % num)


test(100)#实参100
test(200)#实参200


"""
这是内函数---
这是参数---100
这是内函数---
这是参数---200

"""