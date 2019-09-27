#coding=utf-8


class Dog():



    #定义静态方法的场景，不需要访问对象属性/类属性
    @staticmethod
    def run():
        print("小狗在跑....")


#通过类名.调用静态方法，不需要创建对象
Dog.run()