#coding=utf-8

#0,1,1,2,3,5,8,13
nums = list()

a = 0
b = 1
i = 0

while i < 10:
    nums.append(a)
    a , b = b, a + b
    i +=1

for num in nums:
    print(num,end="、")