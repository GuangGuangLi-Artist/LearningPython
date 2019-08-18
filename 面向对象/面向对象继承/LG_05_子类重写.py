#coding=utf-8


class Animal():


    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal):


    def bark(self):
        print("汪汪汪")



class XiaoTianQuan(Dog):


    def fly(self):
        print("我会飞")

    #方法重写

    def bark(self):
        print("叫的和小奶狗一样")



xiaotianquan = XiaoTianQuan()
xiaotianquan.bark()
