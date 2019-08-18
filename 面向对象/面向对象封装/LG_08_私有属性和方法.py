# coding=utf-8
class Women():

    def __init__(self,name):

        self.name = name


        self.__age = 18

    def __secert(self):

        #私有属性在方法内部可以被正常访问
        print("%s的年龄是%d" %(self.name,self.__age))

xiaomei = Women("小美")

#私有属性不允许在外部访问
#xiaomei.__age

#私有方法不允许在外部访问
#xiaomei.__secert()