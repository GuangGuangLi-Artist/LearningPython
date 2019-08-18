#coding=utf-8

class A():

    def test(self):
        print("test方法")


class B():

    def demo(self):
        print("demo方法")

#多继承
class C(A,B):

    pass

#创建子类对象
c = C()


c.demo()
c.test()


