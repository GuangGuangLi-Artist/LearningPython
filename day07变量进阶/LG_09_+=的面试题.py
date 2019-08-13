#coding=utf-8

def demo(num,num_list):
    print("函数开始")

    # num = num + num
    num += num

    #列表变量使用+=，不会做相加再赋值的操作，num_list = num_list + num_list,本质上是在调用列表的的extend方法
    #num_list = num_list + num_list
    num_list += num_list

    print(num)
    print(number_list)
    print("函数执行结束")

number = 9
number_list = [1,2,3]
demo(number,number_list)

print("===========")
print(number)
print(number_list)