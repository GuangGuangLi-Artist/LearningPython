#coding=utf-8

def input_password():

    #提示用户输入密码
    password = input("请输入一个大于8位的密码:")

    #判断用户输入密码的长度，大于8位就返回
    if len(password) >= 8:
        return password

    #如果密码小于8位，就主动抛出异常
    print("主动抛出异常")
    #1>创建异常对象
    ex = Exception("密码不能小于8位数")
    #2>主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
