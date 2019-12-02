#coding=utf-8

from pymysql import *


class JD():
    def __init__(self):
        self.conn = connect(host="localhost",user="root",password="123456",database="jing_dong",charset="utf8")
        self.cur = self.conn.cursor()


    def __del__(self):
        self.cur.close()
        self.conn.close()

    def add_item(self):
        value = input("请输入您要添加的商品:")
        sql = """insert into goods_cates(name) values ("%s")""" % value
        print(sql)
        self.cur.execute(sql)
        self.conn.commit()


def main():
    jd = JD()
    jd.add_item()





if __name__ == "__main__":
    main()