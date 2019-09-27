#coding=utf-8

class A():

    def test(self):
        print("类A的test方法")
    def demo(self):
        print("类A的demo方法")


class B():

    def test(self):
        print("类B的test方法")

    def demo(self):
        print("类B的demo方法")

#多继承
class C(A,B):

    pass

#创建子类对象
c = C()


c.demo()
c.test()

#确定C类的执行顺序
print(C.__mro__)


