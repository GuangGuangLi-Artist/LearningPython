# -*- coding:utf-8 -*-
from functools import reduce

#map 接受两个参数，一个是函数，一个是Iterable,map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def my_f(x):
    return x * x

map_res = map(my_f,list(range(1,10)))
list_map = list(map_res)
print(list_map)

#reduce 把一个函数作用在一个序列[],这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累积计算


def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('13579'))

def char2num1(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}
    return digits[s]


'''利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''

no_normal_name = ['adam', 'LISA', 'barT']

def normalize(name):
    return name[0:1].upper() + name[1:].lower()

normal_name = list(map(normalize,no_normal_name))
print(normal_name)

#可以切片的对象有list,tuple,str
print('adam'[0:2].upper())