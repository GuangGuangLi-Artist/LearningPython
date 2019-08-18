# coding=utf-8

class Gun():

    def __init__(self,model,):

        #枪的型号
        self.model = model

        #子弹的数量
        self.bullet_account = 0

    #添加子弹
    def add_bullet(self,account):

        self.bullet_account += account

    #发射子弹
    def shoot(self):

        #判断子弹的数量
        if self.bullet_account <= 0:
            print("%s没有子弹了..." %self.model)
            return
        #发射子弹 -1
        self.bullet_account -= 3

        #提示发射信息
        print("[%s]突突突... 剩余子弹%d发" %(self.model,self.bullet_account))


class Solider():

    def __init__(self,name):

        #设置姓名
        self.name = name

        #新兵没有枪
        self.gun = None

ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()

xusanduo = Solider("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)