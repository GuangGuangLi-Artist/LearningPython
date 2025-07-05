# -*- coding:utf-8 -*-

names = ['zhangsan','lisi','wangwu','zhangsan']

count = 0
for name in names:
    if name == 'zhangsan':
        count += 1

print(count)

#for 循环
sum = 0
for x in range(101):
    sum += x
print(sum)

#while 循环
while_sum = 0
num = int(input("请输入一个整数: "))
while num > 0 :
    while_sum += num
    num = num - 2
print(while_sum)


