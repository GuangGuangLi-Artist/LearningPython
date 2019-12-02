#coding=utf-8

from pymysql import *



def main():
    conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='123456',charset='utf8')
    cur = conn.cursor()


    for i in range(100000):
        cur.execute("insert into test_index values('ha-%d')" % i)

    conn.commit()

if __name__ == "__main__":
    main()