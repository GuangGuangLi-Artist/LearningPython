#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
定义一个特殊的__slots__变量，来限制该class实例能添加的属性
__slots__ 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
'''

class Student_slot():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    __slots__ = ('name','age')

class Studen_slot_son(Student_slot):
    pass
    __slots__ = ('color')


if __name__ == '__main__':
    s1 = Student_slot('su',25)
    print('%s,%s' %(s1.name,s1.age))
    try:
        s1.score = 99
        print('%s,%s,%s' %(s1.name,s1.age,s1.score))
    except AttributeError:
        print('不在__slots__的不能绑定')

    s1_son = Studen_slot_son('zhangsan',23)
    s1_son.color = 'blue'
    print('s1_son.color:%s' %(s1_son.color)) 
    try:
        s1_son.score = '99'
    except AttributeError:
        print('子类和父类有一个允许的属性才可以') 
