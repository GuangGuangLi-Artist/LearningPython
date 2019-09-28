#coding=utf-8


class MusicPlayer():

    #创建类属性,记录第一个被创建对象的引用
    instance = None

    #类属性标记初始化动作是否被执行
    init_flag = False

    def __new__(cls, *args, **kwargs):


        #判断类属性是否为空对象
        if cls.instance is None:
            #为第一个对象分配内存空间
            cls.instance = super().__new__(cls)

        #返回类属性保存的的对象引用
        return cls.instance


    def __init__(self):

        #判断初始化方法是否被执行过
        if MusicPlayer.init_flag:
            return

        #如果没有执行过，执行初始化动作
        print("播放器初始化")

        #初始化后修改类属性，标记初始化方法已被执行
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)