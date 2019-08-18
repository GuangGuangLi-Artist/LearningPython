# coding=utf-8

class Cat():
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
#可以使用.属性名 利用赋值语句就可以了
tom.name = "Tom"
tom.drink()
tom.eat()
print(tom.name)
#新建蓝猫
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
lazy_cat.name = "大懒猫"
print(lazy_cat.name)

