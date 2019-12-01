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




    @staticmethod
    def print_menu():
        print("1:所有的shangp")
        print("2:所有的分类")
        print("3:所有的品牌")
        print("4:退出程序")
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
                break
            else:
                print("输入有错误")


def main():
    jd = JD()
    jd.run()

if __name__ == "__main__":
    main()