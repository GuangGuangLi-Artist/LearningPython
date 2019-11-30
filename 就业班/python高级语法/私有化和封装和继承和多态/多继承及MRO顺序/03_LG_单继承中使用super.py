#coding=utf-8


class Parent(object):
    def __init__(self,name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self,name,age):
        print('Son1的init开始执行')
        self.age = age
        super().__init__(name)
        print('Son1的init结束被调用')


class GrandSon(Son1):
    def __init__(self,name,age,gender):
        print('GrandSon的init开始执行')
        self.gender = gender
        super().__init__(name,age) # 单继承不能提供全部参数
        print('GrandSon的init结束被调用')



def main():
    gs = GrandSon("苏彪",12,"女")
    print("姓名:", gs.name)
    print("年龄:", gs.age)
    print("性别:", gs.gender)

if __name__ == "__main__":
    main()