#coding=utf-8

from pymysql import *


def main():
    #创建connect连接
    con = connect(host="localhost",port=3306,user="root",password="123456",database="jing_dong",charset="utf8")

    #获取cursor对象
    cur = con.cursor()

    #执行sql语句，并接收返回的数据
    lines = cur.execute("select * from goods")


    #打印受影响的行数
    print("查询到%d条数据" % lines)

    #循环遍历取出每条数据数据
    # for temp in range(lines):
    #     ret = cur.fetchone()
    #     print(ret)



    # 循环遍历取出每条数据数据方法2
    # result = cur.fetchall()
    # for i in range(len(result)):
    #     print(result[i])


    #取出所有的数据
    result = cur.fetchall()
    print(result)



    #关闭cursor对象
    cur.close()
    #关闭connect对象
    con.close()

if __name__ == "__main__":
    main()