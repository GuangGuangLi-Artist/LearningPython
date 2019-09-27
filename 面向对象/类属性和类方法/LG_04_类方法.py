#coding=utf-8


class Tools():

    #使用赋值语句定义类属性，记录所有工具对象的方法
    count = 0


    #定义类方法

    @classmethod
    def show_tools_count(cls):
        print("工具的总数是 %d" %cls.count)


    def __init__(self,name):
        self.name = name

    #让类的属性值加1

        Tools.count += 1


#创建工具对象
tool1 = Tools("斧头")
tool2 = Tools("铲子")
tool3 = Tools("枪")


#调用类方法
Tools.show_tools_count()