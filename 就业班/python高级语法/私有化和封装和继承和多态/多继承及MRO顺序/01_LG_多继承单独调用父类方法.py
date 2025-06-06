#coding=utf-8


print("---多继承使用类名.__init__发生的状态---")

class Parent(object):
    def __init__(self,name):
        print("parent的init开始被调用")
        self.name = name
        print("parent的init结束被调用")


class Son1(Parent):
    def __init__(self,name,age):
        print("Son1的init开始被调用")
        self.age = age
        Parent.__init__(self,name)
        print("Son1的init结束被调用")


class Son2(Parent):
    def __init__(self,name,gender):
        print("Son2的init开始被调用")
        self.gender = gender
        Parent.__init__(self, name)
        print("Son2的init结束被调用")


class GrandSon(Son1,Son2):
    def __init__(self,name,age,gender):
        print("GrandSon的init开始被调用")
        Son1.__init__(self, name,age)
        Son2.__init__(self,name,gender)
        print("GrandSon的init结束被调用")

def main():
    gs = GrandSon('苏彪',12,"男")
    print("姓名:",gs.name)
    print("年龄:", gs.age)
    print("性别:", gs.gender)


if __name__ == "__main__":
    main()