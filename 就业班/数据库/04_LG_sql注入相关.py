#coding=utf-8

from pymysql import *


class JD():
    def __init__(self):
        self.conn = connect(host="localhost",user="root",password="123456",database="jing_dong",charset="utf8")
        self.cur = self.conn.cursor()


    #对象销毁时执行这个方法断开数据库连接
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cur.execute(sql)
        for temp in self.cur.fetchall():
            print(temp)

    def show_all_items(self):
        sql = "select * from goods"
        self.execute_sql(sql)

    def show_all_cate(self):
        sql = "select name from goods_cates "
        self.execute_sql(sql)

    def show_all_brand(self):
        sql = "select name from goods_brand "
        self.execute_sql(sql)

    def get_info_by_name(self):
        # name=input("请输入要查询的商品的名字:")
        # #不安全的sql输入: ' or 1=1 or '1
        # sql = """select * from goods where name = '%s';""" % name
        # print("------->>%s<<<-------" % sql)
        # self.execute_sql(sql)


        #安全方式  防止sql注入
        find_name = input("请输入要查询的商品的名字:")
        sql = "select * from goods where name=%s"
        self.cur.execute(sql,[find_name])
        print(self.cur.fetchall())





    @staticmethod
    def print_menu():
        print("1:所有的shangp")
        print("2:所有的分类")
        print("3:所有的品牌")
        print("4:根据名字查")
        print("5:退出程序")
        return input("请输入你想查询的内容")

    def run(self):
        while True:
            num =self.print_menu()
            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.show_all_cate()
            elif num == "3":
                self.show_all_brand()
            elif num == "4":
                self.get_info_by_name()
            elif num == "5":
                break
            else:
                print("输入有错误")


def main():
    jd = JD()
    jd.run()

if __name__ == "__main__":
    main()