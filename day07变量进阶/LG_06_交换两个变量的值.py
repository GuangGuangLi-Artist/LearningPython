#coding=utf-8

a = 6

b = 100

#使用其他变量

# c = a
#
# a = b
#
# b = c
#
# print(a)
# print(b)


#不使用其它变量

#
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)


#python方法
#a,b = (b,a)
a,b = b,a #上边代码的简化，等号右边是元组，只是把（）隐藏了
print(a)
print(b)