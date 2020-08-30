#coding=utf-8

def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


fact = factorial
m = fact(5)
print(m)