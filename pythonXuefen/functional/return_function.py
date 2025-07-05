# -*- coding:utf-8 -*-

#把函数作为返回值返回
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

lazy_res = lazy_sum(1,3,5)
print(lazy_res())

print('------------')

'''闭包
内部函数可以引用外部函数的参数和局部变量，当外部函数返回内部函数时，相关参数和变量都保存在返回的函数中
返回闭包时牢记一点，返回函数不要引用任何循环变量，或者后续会发生变化的变量
如果一定需要引入循环变量，方法就是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
已绑定到函数参数的值不变
'''

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
f1,f2,f3, = count()
print(f1())
print(f2())
print(f3())

print('------------')

def new_count():
    def f_new(j):
        def g_new():
            return j * j
        return g_new
    fs_new = []
    for i in range(1,4):
        fs_new.append(f_new(i)) # fs_new() 立刻执行，因此i的当前值被传入f()
    return fs_new

f1_new,f2_new,f3_new = new_count()
print(f1_new())
print(f2_new())
print(f3_new())
print('------------')
#nonlocal 
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。 

def inc():
    x = 0
    def fn():
        #仅读取x的值
        return x + 1
    return fn
fc = inc()
print(fc())
print(fc())
print('------------')
def inc_new():
    x = 0
    def fn_new():
        nonlocal x
        x = x + 1
        return x
    return fn_new
fc_new = inc_new()
print(fc_new())
print(fc_new())
print('------------')
#练习 利用闭包返回一个计数器函数，每次调用它返回递增整数

def createCounter():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter

countA = createCounter()
print(countA(),countA(),countA(),countA())

