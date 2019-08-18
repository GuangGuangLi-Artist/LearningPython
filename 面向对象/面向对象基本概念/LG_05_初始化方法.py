# coding=utf-8

class Cat():

    def __init__(self):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值 就可以 定义属性
        self.name = "Tom"

    def eat(self):
        print("%s爱吃鱼" %self.name)



#初始化方法在创建对象时会被自动调用
tom = Cat()
print(tom.name)
tom.eat()