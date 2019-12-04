#coding=utf-8

#字符串转换成列表
a = "[1,2,3,4,5,6]"
print(type(a))
b = eval(a)
print(b)
print(type(b))


print("====" * 30)


#字符串转换成字典
x = "{1:'李广',2:'苏彪',3:'陈诚'}"
print(type(x))
y = eval(x)
print(y)
print(type(y))

print("====" * 30)

#字符串转换成元组
m = "([1,2],{3:'liguang'},(4.6),7,'123')"
print(type(m))
n = eval(m)
print(n)
print(type(n))

print("====" * 30)

#eval()函数传进去的参数必须是对象或者字符串

aa = 10
print(eval("aa + 1"))
print("====" * 30)
bb = 10
print("bb")
cc = {"bb":4}
print(eval("bb+1",cc))



