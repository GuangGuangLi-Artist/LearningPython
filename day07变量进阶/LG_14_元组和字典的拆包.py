# coding=utf-8


def demo(*args,**kwargs):


    print(args)
    print(kwargs)

#定义元组/字典

set_yuanzu = (1,2,3)
set_dict = {"name":"liguang","age":"18"}

#拆包语法，作用是简化元组/字典参数的传递
demo(*set_yuanzu,**set_dict)
