# -*- coding:utf-8 -*-

import math

print(abs(-1))

print(max(1,3,5))
print(int('123'))
print(float('1.23'))
print(str(1.23))
print(bool('123'))

#平方根
print(math.sqrt(2))

def myabs(x):
    if x >= 0:
        return x
    else:
        return -x

#print(myabs(int(input("请输入一个正数或者负数: "))))

def my_move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

print(my_move(100,100,60,math.pi / 6))

#默认参数  选填参数在前，默认参数在后
def my_pow(x,n=3):
    res = 1
    while n > 0:
        n = n - 1
        res = res * x
    return res

print("3的立方：", my_pow(3))
print(my_pow(2,4))

# 默认参数必须指向不可变对象
def add_end_havepro(L=[]):
    L.append("END")
    return L

print(add_end_havepro())
print(add_end_havepro())
print(add_end_havepro())

def add_end_nopro(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

print(add_end_nopro())
print(add_end_nopro())
print(add_end_nopro())


#可变参数 在函数内部 nums接受的是一个tuple

def my_calc(*nums):
    sum = 0
    for x in nums:
        sum = sum + x * x
    
    return sum

print(my_calc(1,3))

# 将已存在的list或者tuple转为可变参数传递
self_num_list = [1,2,3]
print(my_calc(*self_num_list))

#关键字参数 
def my_person(name,age,**kw):
    print('name:' ,name," age:",age,' other:',kw)

my_person('zhangsan','20')
my_kw_dict = {'city':'xian','gender':'男'}
my_person('lisi','18',**my_kw_dict)
my_person('wangwu','28',city=my_kw_dict['city'],gender=my_kw_dict['gender'])

#命名关键字参数
def name_key_param(name,age,*,city='xian',gender):
    print('name:' ,name," age:",age,' city:',city,' city:',gender)

name_key_param('huanghe',18,city='hangzhou',gender='女')
name_key_param('huanghe1',28,gender='女')

'''
函数的参数有五种，分别是位置参数，默认参数,可变参数,关键字参数,命名关键字参数
其中，可变参数无法和命名关键字参数混合
函数中传递的顺序是 位置参数，默认参数,可变参数/命名关键字参数和关键字参数

'''

def combine_fun_1(a,b,c=0,*args,**kw):
    print("a:",a,"b:",b,"c:",c,"agrs:",args,"kw:",kw)

def combine_fun_2(a,b,c=0,*, d,**kw):
    print("a:",a,"b:",b,"c:",c,"d:",d,"kw:",kw)

combine_fun_1('a','b','3',*(5,6),kw={"name":"zhangsan"})
combine_fun_1('a','b','3',5,6,name='zhangsan')
combine_fun_1('a','b')

combine_fun_2('aa','bb',d='zhansan',name='kawayi')

com_agrs = ('aaa','bbb','ccc','ddd')
com_kw ={'name':'wuyi','gender':'nv'}
com_fun2=('aaa','bbb','ccc')
com_kw2 ={'d':'ddd','gender':'nv'}

combine_fun_1(*com_agrs,**com_kw)
combine_fun_2(*com_fun2,**com_kw2)


#递归函数
def digui_fun(n):
    if n == 1:
        return 1
    return n * digui_fun(n-1)

print(digui_fun(100))