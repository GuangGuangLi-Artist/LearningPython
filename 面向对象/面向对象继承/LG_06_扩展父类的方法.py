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

    #扩展
    def bark(self):

        #1针对子类特有的需求，编写代码
        print("像小奶狗一样叫唤")

        #2使用super()，调用原来在父类中封装的方法,
        #推荐使用
        super().bark()


        #父类名.方法(self)
        #不推荐
        #Dog.bark(self)

        #3增加其他子类的代码
        print("@#$%^&*()(*^$#$%^&")



xiaotianquan = XiaoTianQuan()
xiaotianquan.bark()
