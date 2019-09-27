#coding=utf-8


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



#查看游戏的帮助信息

Game.show_help()


#创建历史最高分

Game.show_top_score()

#创建游戏对象
game = Game("李广")

game.start_game()