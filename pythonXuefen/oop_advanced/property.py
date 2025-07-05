#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@property装饰器就是负责把一个方法变成属性调用的
    例子是Student_countAge
    birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
    属性的方法名不要和实例变量重名，属性方法名和实例变量重名，会造成递归调用，导致栈溢出报错！
    例如 如下代码是错误的 
        @property
        def birth(self):
            return self.birth
    
    


'''

import datetime
class Student_property():
    
    def get_score(self):
        return self._score
    
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be  an int number')
        if value < 0 or value > 100:
            raise ValueError('score  must between 0~100')
        self._score = value
        

class Student_countAge():

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self,value):
        if not isinstance(value,int):
            raise ValueError('birth must be  an int number')
        if value < 0 or value > 3000:
            raise ValueError('birth  must between 0~100')
        self._birth = value

    @property
    def age(self):
        return datetime.date.today().year - self._birth


if __name__ == '__main__':
    sp = Student_property()
    try:
        sp.set_score(999)
    except ValueError as e: 
        print(e)

    print('------------')

    sc = Student_countAge()
    sc.birth = 1993
    print('当前年龄是:%s' % sc.age)

     