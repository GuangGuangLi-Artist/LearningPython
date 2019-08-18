# coding=utf-8

class Person():

    def __init__(self,name,weight):

        #self.属性=形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字是%s,体重是%.2f公斤" %(self.name,self.weight)

    def run(self):
        print("%s爱跑步,跑步锻炼身体" %(self.name))

        self.weight -= 0.5

    def eat(self):
        print("%s吃东西涨体重" %(self.name))

        self.weight += 1

xiaoming = Person("小明",75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

#小美爱跑步
xiaomei = Person("小美",45.0)
xiaomei.eat()
xiaomei.run()
print(xiaomei)