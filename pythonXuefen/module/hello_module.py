#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


'''作用域
__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
__xxx和_xxx这样的函数或变量就是非公开的（private），不应该被直接引用，如果要引用这种'不应该'被直接引用的变量，一般需要提供一个
方法，使用这个方法去调用
'''

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

'''
__name__ 
    1.如果是本函数直接执行,python hello_module.py 就是'__main__'
    2.如果是被其他模块引用，比如被hello.py,运行hello.py python hello.py,就是‘hello_module’ 
'''
print(__name__)  

if __name__=='__main__': 
    test()
    greetres = greeting('dan')
    print(greetres)