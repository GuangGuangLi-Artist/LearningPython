#coding=utf-8


class Pro(object):

    #类属性
    Country = "中国"

    def __init__(self,name,gdp):
        #实例属性
        self.name = name
        self.gdp =gdp


    #类方法
    @classmethod
    def change_country(cls,country):
        cls.Country = country

    #静态方法
    @staticmethod
    def static_test():
        print("静态方法")

    #实例方法
    def show_gdp(self):
        print("%s的gdp收入是%d" %(self.name,self.gdp))

gs = Pro("甘肃",100010000)
#访问实例属性
print(gs.gdp)
print(gs.name)
#对象访问类属性
print(gs.Country)
#直接访问类属性
print(Pro.Country)

print("*" * 50)


#对象访问实例方法
gs.show_gdp()

#对象访问静态方法
gs.static_test()

#对象访问类方法
gs.change_country("中国2")
print(gs.Country)

print("------")
#类访问类方法
Pro.change_country("中国国")
print(Pro.Country)


#类访问静态方法
Pro.static_test()





