# -*- coding:utf-8 -*-

'''
lambda
冒号前面的值 表示函数参数
'''
#在map()函数中传入lambda函数
print(list(map(lambda x: x * x,list(range(1,5)))))
#把匿名函数赋值给一个变量，再利用变量调用函数
print('-----------')
f_lambda= lambda x : x * x
print(f_lambda(5))

#把匿名函数作为返回值返回
def build_lambda(x,y):
    return lambda: x * x + y * y
print('-----------')
build_res = build_lambda(2,5)
print(build_res()) 

#使用匿名函数改造下面的代码
'''
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print(L)
'''
list_lambda_ac = list(filter(lambda x: x % 2 == 1,range(1,20)))
print(list_lambda_ac)

