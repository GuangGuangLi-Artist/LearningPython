# -*- coding:utf-8 -*-

names = ['zhangsan','lisi','wangwu','zhangsan']

print(len(names))
#正序
names.sort()
print(names)
#倒序
names.reverse()
print(names)
names.append('su')
print(names)
#有几个
print(names.count("zhangsan"))
print(names.index('su'))

#删除指定位置
names.pop(1)
print(names)

#指定位置添加
names.insert(0,'qinshihuang')
print(names)

#二维数组
code_languages = ['java','python','c++',['html','css','javascript'],'go','php']
print(code_languages)
print(code_languages[3])

#元组 一旦初始化就不能修改

names_tuple = ('zhangsan','lisi','wangwu','zhangsan')
print(names_tuple)
one_ele_tuple = (1,)
print(one_ele_tuple)

#tuple中的索引2处是可变的数组，tuple不可变是指2指向的索引不变，指向的可变元素可以变
nochange_tuple = ('a','b',['A','B'])
print(nochange_tuple[2][0],'----',nochange_tuple[2][1])
print(nochange_tuple)
nochange_tuple[2][0] = 'X'
nochange_tuple[2][1] = 'Y'
print(nochange_tuple[2][0],'----',nochange_tuple[2][1])
print(nochange_tuple)

try:
    nochange_tuple[0] = 'x' # 'tuple' object does not support item assignment
except TypeError as typeError:
    print('TypeError',typeError)
finally:
    print(nochange_tuple)



if 'zhangsan1' not in names:
    print("张三不在")
elif 'lis' in names:
    print(names)
else:
    print("都不在")


if names:
    print('true')

input_year = input('请输入年份: ')
# int() 将字符串转换成数字
int_year = int(input_year)

if int_year > 2000:
    print('00后')
else:
    print('00前')


