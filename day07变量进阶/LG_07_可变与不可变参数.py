#coding=utf-8
"""
无论传递的参数是 **可变** 还是 **不可变**

- 只要 **针对参数** 使用 **赋值语句**，会在 **函数内部** 修改 **局部变量的引用**，**不会影响到 外部变量的引用**
"""

def demo(num,num_list):
    print("函数内部的代码")

    #在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    num = 100
    num_list = [1,2,3]
    print(num)
    print(num_list)
    print("函数执行完成")

gl_num = 99
gl_numlist = [4,5,6]
demo(gl_num,gl_numlist)
print(gl_num)
print(gl_numlist)