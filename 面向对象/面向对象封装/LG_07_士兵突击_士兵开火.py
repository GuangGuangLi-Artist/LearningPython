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

    def fire(self):

        #判断士兵是否有枪
        #if self.gun == None:在 Python 中针对 None 比较时，建议使用 is 判断
        #身份运算符用于 比较 两个对象的 内存地址 是否一致 —— 是否是对同一个对象的引用
        if self.gun is None:
            print("%s没有枪..." %(self.name))
            return


        #高喊口号
        print("我[%s]要冲啊..." %(self.name))

        #许三多让枪装填子弹
        self.gun.add_bullet(50)


        #士兵用枪射击

        self.gun.shoot()


#创建枪对象
ak47 = Gun("ak47")

#创建士兵
xusanduo = Solider("许三多")
xusanduo.gun = ak47
#士兵射击
xusanduo.fire()