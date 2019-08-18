# coding=utf-8

class Cat():
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.drink()
tom.eat()
#新建蓝猫

lazy_cat = Cat()
lazy_cat2 = lazy_cat

lazy_cat.drink()
lazy_cat.eat()

print(tom)
print(lazy_cat)
print(lazy_cat2)

print(id(tom))
print(id(lazy_cat))
print(id(lazy_cat2))