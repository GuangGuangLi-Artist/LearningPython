#coding=utf-8



'''
使用私有property升级getter和setter方法
'''

class Money(object):

    def __init__(self):
        self.__money_count = 10000000

    def getMoney(self):
        return self.__money_count


    def setMoney(self,value):
        if isinstance(value,int):
            self.__money_count = value
        else:
            print("error:不是整形数字")

    # 定义一个属性，当对这个money设置值时调用setMoney,当获取值时调用getMoney
    money = property(getMoney,setMoney)

a = Money()
t = a.money
print(t)
a.money = 12000000
print(a.money)
