# -*- coding:utf-8 -*-

'''
函数式编程
允许把函数本身作为参数传入另一个函数，还允许返回一个函数
'''

# 高阶函数
'''
1、变量可以指向函数
2、函数名也是变量
3、传入函数
'''
f = abs
print(f(-10))

# abs = 10
# #TypeError: 'int' object is not callable
# print(abs(-10)) 
print('----------')
def add_f(x,y,f):
    return f(x) + f(y)


print(add_f(5,-6,f))
