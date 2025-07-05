# -*- coding:utf-8 -*-

dict_names = {'zhangsan':100,'lisi':85,'wangwu':80,'zhangsan':95,'su':98}
print(dict_names['zhangsan'])

dict_names['lihaha'] = 99
print(dict_names)

print(dict_names.keys())
print(dict_names.values())
print(dict_names.items())
print(dict_names.get('lihaha'))
print(dict_names.pop('lihaha'))
print(dict_names)

for k,v in dict_names.items():
    print("name:", k , "value:", v)


set_1 = set([1,2,3,4,4,5])
print(set_1)
set_2 = set([2,3,4,5])
set_2.add(6)
print(set_2)
set_2.pop() #从头删除第一个元素
print(set_2)
set_2.remove(3)
print(set_2)

print(set_1 & set_2)
print(set_1 | set_2)

'''
可变不可变  
对于不可变对象来说，调用对象自身的任意方法，不会改变该对象自身，相反们这些方法会创建新的对象并返回，
这样，就保证了不可变对象本身永远是不变的
'''
list_a = ['a','c','b']
list_a.sort()
print(list_a)
str_a = 'acb'
str_rep = str_a.replace('a','A')
print(str_a)
print(str_rep)



