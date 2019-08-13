# coding=utf-8

def sum_number(number):


    print(number)
    #递归的出口，当函数满足某个条件时，函数不再执行
    if number == 1:
        return
    #函数自己调用自己
    sum_number(number-1)


sum_number(3)