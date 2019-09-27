#coding=utf-8
'''
案例小结
实例方法 —— 方法内部需要访问 实例属性
实例方法 内部可以使用 类名. 访问类属性
类方法 —— 方法内部 只 需要访问 类属性
静态方法 —— 方法内部，不需要访问 实例属性 和 类属性
'''


class Game():


    #定义类属性
    top_score = 0

    #定义实例属性
    def __init__(self,player_name):
        self.player_name = player_name

    #定义静态方法
    @staticmethod
    def show_help():
        print("帮助信息-----让僵尸走进来")


    #定义类方法
    @classmethod
    def show_top_score(cls):
        print("历史最高分是 %d" %(cls.top_score))


    #定义实例方法
    def start_game(self):
        print("%s 开始游戏啦" % (self.player_name))


        #使用类名修改历史最高分
        Game.top_score = 99



#查看游戏的帮助信息

Game.show_help()


#创建历史最高分

Game.show_top_score()

#创建游戏对象
game = Game("李广")

game.start_game()


#游戏结束，查看最高分
Game.show_top_score()