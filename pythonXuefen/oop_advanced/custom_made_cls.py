#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from enum import Enum,unique
'''
定制类
    1、__str__ 返回一个规定格式的字符串
    2、__iter__ 返回一个迭代对象，使用__next__()调用
    3、__getitem__  如果在类中定义了__getitem__()方法，那么他的实例对象（假设为P）就可以这样P[key]取值。
    4、__getattr__  只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。 
    5、__call__   任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
    6、枚举类 Enum

'''
class Student_str():
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return 'Student_str object (name:%s)' % self.name
    
    __repr__  = __str__

class Fib_iter():
    def __init__(self):
        
        self.a,self.b = 0,1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 5:
            raise StopIteration
        return self.a
    
class Fib_slice_getittem():
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L
        
class Student_getattr():
    def __init__(self):
        self.name = 'Guang'
    
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        
        if attr == 'age':
            return lambda:25

class Chain_attr():
    def __init__(self,path=''):
        self._path = path
    
    def __getattr__(self,path):
        return Chain_attr('%s/%s' %(self._path,path))
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__

class Student_call():
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('my name is %s' %(self.name))

@unique
class Weekday_enum(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6




        


if __name__ == '__main__':
    ss = Student_str('zhang')
    print(ss)#<__main__.Student_str object at 0x000001D9EDB99CA0>
    print(ss) #Student_str object (name:zhang) 

    for i in Fib_iter():
        print(i)

    #print(Fib_iter()[3]) #TypeError: 'Fib_iter' object is not subscriptable
    f = Fib_slice_getittem()
    print(f[1:3])
    print(f[:10])
    print('--------------')
    sa = Student_getattr()
    print(sa.name)
    print(sa.score) #AttributeError: 'Student_getattr' object has no attribute 'score'
    print(sa.age())
    print(Chain_attr().status.user.timeline.list)

    sc = Student_call('li')
    sc()
    print(callable(Student_call('c')))
    print(callable(max))
    print(callable(None))

    print('--------------')
    day1 = Weekday_enum.Mon
    print(day1)
    print(Weekday_enum.Thu)
    print(Weekday_enum.Fri.value)
    print(Weekday_enum['Sat'])



