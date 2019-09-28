#coding=utf-8


try:
    num = int(input("请输入一个整数:"))

    result = 8 / num

    print(result)

except ValueError:
    print("请输入一个整数")

except ZeroDivisionError:
    print("除数不能为0")

