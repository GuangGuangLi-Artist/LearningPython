#coding=utf-8

def demo(gl_list):

    print("函数内部的代码")

    gl_list.append(9)

    print(gl_list)

    print("函数执行完毕")

num_list  = [1,2,3]
demo(num_list)
print("===============")
print(num_list)