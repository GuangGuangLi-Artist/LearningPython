# -*- coding:utf-8 -*- 


import functools
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int2 = functools.partial(int,base=2)
print(int2('101'))
print(int2('101',base=10)) #kw={'base':2}

max2 = functools.partial(max,10) #args=10
print(max2(3,6,8))