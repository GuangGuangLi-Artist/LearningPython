#coding=utf-8


class MusicPlayer():

    #创建类属性,记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):


        #判断类属性是否为空对象
        if cls.instance is None:
            #为第一个对象分配内存空间
            cls.instance = super().__new__(cls)

        #返回类属性保存的的对象引用
        return cls.instance


player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)