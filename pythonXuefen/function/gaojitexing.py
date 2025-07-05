# -*- coding:utf-8 -*-

import os

'''切片'''
L = ['python','java','javascript','html','css','go','php']
litotu = tuple(list(range(20)))

#取索引从零开始元素，直到索引3结束，不包含3
print(L[0:3])

#负数取 从尾部取
print(L[-3:-1])
print(L[-3:])

int_l = list(range(100))

# 前十个
print(int_l[:10])

#前十个 步长为2
print(int_l[:10:2])

#10-20步长为3
print(int_l[10:20:3])

# 步长为5
print(int_l[::5])

#复制
print(int_l[:])

print(litotu[::2])


'''迭代

python可以迭代所有的可迭代对象
'''
#enumerate函数能够将list变成索引-元素对
print(enumerate(L))
for k,v in enumerate(L):
    print(k,':',v)

print('---------')
for x,y in [(1,'a'),(2,'b'),(3,'c')]:
    print(x,':',y)

#列表生成式
print([x * x for x in range(1,11) if x % 2 == 0])
#双层循环
print([m + n for m in 'ABC' for n in 'XYZ'])


print([d for d in os.listdir('.')])

dict_it = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k,v in dict_it.items()])

#生成器
#一边循环 一边计算的机制 就是生成器
my_generator = (x * x for x in range(1,11) if x % 2 == 0)
print(next(my_generator))
print(next(my_generator))

print('------------')
def my_gennerator_func():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


'''
生成器函数和普通函数执行流程的区别
普通函数顺序执行，生成器函数每次通过next()函数调用执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
'''
my_g_f = my_gennerator_func()

for i in my_g_f:
    print(i)
print('------------')
# 再次调用就会因为没有yield可以执行了 报StopIteration
#print(next(my_g_f))

'''迭代器
可迭代对象Iterable 
    list、tuple、dict、set、str、generator、generator function

可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
list、dict、str 等Iterable变成Iterator可以使用iter()函数 
'''

str_test = 'abcdef'
str_ite = iter(str_test)
#for 循环本质尚就是不断调用next()函数实现

while True: 
    try:
        print(next(str_ite))
    except StopIteration:
        break

for i in str_ite:
    print(i)

