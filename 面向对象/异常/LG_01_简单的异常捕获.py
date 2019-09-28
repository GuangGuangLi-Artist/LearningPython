#coding=utf-8

try:
    #不能确定是否正常执行的代码
    num = int(input("请输入一个整数:"))
    print(num)
except:
    #处理异常的代码
    print("请输入正确的数字")

print("---" * 50)
