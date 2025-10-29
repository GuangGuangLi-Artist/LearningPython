#coding=utf-8

#把元组用作记录
city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print("%s/%s" %passport)
print("--" * 20)

#for循环分别提取元组里的元素,也叫做拆包,可以使用“_”作为占位符
for country,_ in traveler_ids:
    print(country)
print("--" * 20)

for country_1,passport_num in traveler_ids:
    print(country_1,passport_num)
    print(country_1)
    print(passport_num)
print("--" * 20)

#平行赋值
lax_coordinates = (33.9425,-118.408056)
latitude,longitude = lax_coordinates
print('latitude:',latitude,',longitude:',longitude)
print("--" * 20)

#交换变量的值
a = 5
b = 10
a,b = b,a
print('a:',a,',b:',b)
print("--" * 20)

#函数返回多个值
def min_max(items):
    return min(items),max(items)
print(min_max([1,2,3,4,5,6,7,8,9]))
print("--" * 20)

#使用*运算符把一个迭代对象拆开作为函数的参数
t = (20,8)
print(divmod(20,8))#divmod函数返回商和余数
print(divmod(*t))
quotient,remainder = divmod(*t)
print('quotient:',quotient,',remainder:',remainder)
print("--" * 20)

#让一个函数可以用元组的新式返回多个值，然后调用函数的代码就能轻松接受这些返回值
import os
_,filename = os.path.split('E:/pythonWorkspace/LearningPython/fluentpython/02-array-seq/05-元组数据记录.py')
print('filename:',filename)
print("--" * 20)

#使用*来处理剩下的元素

a,b,*rest = range(5)
print('a:',a,',b:',b,',rest:',rest)
a,b,*rest = range(3)
print('a:',a,',b:',b,',rest:',rest)
a,b,*rest = range(2)
print('a:',a,',b:',b,',rest:',rest)
print("--" * 20)
#在平行赋值中，*前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
a,*body,c,d = range(5)
print('a:',a,',body:',body,',c:',c,',d:',d)
*head,b,c,d = range(5)
print('head:',head,',b:',b,',c:',c,',d:',d)
print("--" * 20)
#嵌套元组拆包