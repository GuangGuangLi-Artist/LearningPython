#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import types
'''
1、类和实例
    数据封装
2、访问限制
    内部属性要是想不被外部访问,可以在属性的名称前加上两个__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    #__name可以通过'_类名__属性名访问' 但是强烈建议不这么访问
3、继承和多态
    继承有什么好处，最大的好处是子类获得了父类的全部功能
    当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
    多态的好处是我们调用run_twice(),只要是Animal的子类,是Animal类型，就会调用子类对象的实际的run()方法
    开闭原则：
        对扩展开放：允许新增Animal子类；
        对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
4、获取对象信息
    type() 判断对象类型
    isinstance() 判断对象类型
        总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
    dir() 获得一个对象的所有属性和方法 返回一个包含字符串的list
        __len__方法返回长度
        配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
5、实例属性和类属性
    编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
    再使用相同的名称，访问到的将是类属性。
    例子 Animal的 class_attr
    实例属性属于各个实例所有，互不干扰；
    类属性属于类所有，所有实例共享一个属性；



'''

class Animal:

    #类属性
    class_attr = '类属性'

    def __init__(self,name,age,color):
        self.__name = name
        self.__age = age
        self.__color = color
        self.teeth_count = 9  

    def set_name(self,name):
        self.__name = name
    
    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def _print_age(self): #单个_代表'不应该'被直接引用
        print('%s现在%d岁了' %(self.__name,self.__age))

    def run(self):
        print('Animal is running')

    def __len__(self):
        return 100


    
    
class Dog(Animal):

    def run(self):
        print('%s dog is running' %(self.get_name()))

class Cat(Animal):
    def run(self):
        print('%s cat is running' %(self.get_name()))

class Husky(Dog):
    pass


def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print('%s is running slowly...' %(self.get_name()))


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')



print('------------')
if __name__ == '__main__':
    dog = Animal('heibao',25,'blue')
    print(dog.get_name())
    print(dog.get_age())
    print(dog._Animal__name)#__name可以通过'_类名__属性名访问' 但是强烈建议不这么访问
    try:
        print(dog.__color)
    except AttributeError:
        print('外部不能直接获取__开头的私有变量')
    print('------------')
    dog.set_name('黑豹')
    print(dog.get_name())
    dog._print_age()

    print('------------')

    #继承的案例
    cat_shanfu = Cat('杉伏',2,'黑灰')
    #多态
    cat_shanfu.run()

    #演示多态的好处
    run_twice(Animal('丑狗',2,'黑色'))
    run_twice(Dog('波利',12,'黑色'))
    run_twice(Tortoise('忍者',12,'黑色'))



    print('------------')
    a = list()
    print(isinstance(a,list))
    print(isinstance(dog,Animal))
    print(isinstance(cat_shanfu,Cat))
    print(isinstance(cat_shanfu,Animal))# 猫是动物
    print(isinstance(dog,Cat))#动物不是猫

    print(type(123))#<class 'int'>
    print(type('str'))#<class 'str'>
    print(type(None))#<class 'NoneType'>
    print(type(True))#<class 'bool'>

    print('--------')

    def fn(a,b):
        return a * b

    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda a: a) == types.LambdaType)
    print(type((x for x in range(1,10))) == types.GeneratorType)

    print('--------')

    a = Animal('dog',15,'blue')
    b = Cat('dog',1,'green')
    h = Husky('huskyDog',5,'red')

    print(isinstance(h,Husky))
    print(isinstance(h,Dog))
    print(isinstance(h,Animal))
    print(isinstance(h,Animal) and isinstance(h,Cat))
    print(isinstance(b'a',bytes))
    print(isinstance(123,int))
    print(isinstance([1,2,3],(list,tuple)))
    print('------------')
    print(dir('ABC'))
    '''
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
    '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
    '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', 
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
    '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
    'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
    'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
    'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
    'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
    'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    '''
    print('ABC'.__class__)
    print('ABC'.__contains__('A'))
    print('ABC'.center(0))
    print('ABC'.count('A'))
    print('ABC'.endswith('A'))
    print('ABC'.__doc__)
    print('ABC'.__len__())
    print('------------')
    print(len(dog))
    print(hasattr(dog,'teeth_count'))
    print(hasattr(dog,'__name'))#false
    print(dog.teeth_count)
    setattr(dog,'tail','long')
    print(hasattr(dog,'tail'))
    print(getattr(dog,'tail'))
    print(getattr(dog,'foot',404))#不存在属性时传入一个default参数，如果属性不存在，就返回默认值
    print(getattr(dog,'run'))

    dog_run = getattr(dog,'run')# 获取属性'run'并赋值到变量dog_run
    dog_run()

    print('------------')
    print(dog.class_attr)#实例没有class_attr属性，打印了类的class_attr
    print(Animal.class_attr)#类属性
    dog.class_attr = '实例属性' #实例绑定属性class_attr
    print(dog.class_attr)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    print(Animal.class_attr)#类属性并未消失，用Animal.class_attr仍然可以访问
    del dog.class_attr #删除实例的class_attr属性
    print(dog.class_attr)#再次调用，实例没有class_attr属性，类的class_attr属性就可以显示了










    def _print_name(name):
        print(name)
    print('------------')
    _print_name('张丹')

