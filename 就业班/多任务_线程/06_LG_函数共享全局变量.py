#coding=utf-8

#在一个函数中对全局变量进行修改时，到底是否需要使用global,要看是否对全局变量的指向进行了修改，如果修改了指向，即让
#全局变量指向了一个新的地方，那么必须使用global，如果时修改了指向的空间的数据，那么就不用必须使用global

num = 100
num_list = [11,22]

def test():
    global  num
    num += 100

def test2():
    num_list.append(33)

print(num)
print("-----" * 50)
test()
print(num)
print("-----" * 50)
print(num_list)
print("-----" * 50)
test2()
print(num_list)