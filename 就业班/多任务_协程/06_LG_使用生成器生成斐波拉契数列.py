#coding=utf-8

def fib(all_num):

    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print(a)
        a, b = b, a + b
        current_num +=1

fib(10)