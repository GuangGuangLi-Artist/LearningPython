#coding=utf-8


lax_coordinates = (33.9425,-118.408056)
#元组拆包
latitude,longitude = lax_coordinates

print(latitude)
print(longitude)

print("*" * 20)

(a,b) = (20,30)
print(a)
print(b)
#不使用中间变量交换两个变量的值
b,a = a,b
print("*" * 20)
print(a)
print(b)

print("*" * 20)
#使用*运算符将一个迭代对象拆开作为函数的参数
x = divmod(20,8)
print(x)
t = (20,8)
y = divmod(*t)
print(y)
quotient,remainder = divmod(*t)
print(quotient,remainder)

#让一个函数可以用元组的新式返回多个值，然后调用函数的代码就能轻松接受这些返回值
import os
_,filename = os.path.split('E:/pythonWorkspace/LearningPython/fluentpython/02-array-seq/05-元组数据记录.py')
print(filename)

print("*" * 20)

#使用*来处理剩下的元素
a,b,*rest = range(5)
print(a,b,rest)
a,b,*rest = range(3)
print(a,b,rest)
a,b,*rest = range(2)
print(a,b,rest)

#在平行赋值中，*前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
a,*body,c,d = range(5)
print(a,body,c,d)
*head,b,c,d = range(5)
print(head,b,c,d)

#嵌套元组拆包
metro_areas = [
    ('Tokys','JP',36.933,(35.689722,139.691667)),
    ('Delhi','NCR',21.935,(28.689722,77.691667)),
    ('New York-Newark','US',20.933,(19.689722,-99.691667)),
    ('Sao Paulo','BR',19.933,(-23.689722,-46.691667))
]
print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name,cc,pop,(latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))

