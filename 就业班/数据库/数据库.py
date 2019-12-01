#coding=utf-8

from pymysql import *

#192.168.0.104


# 创建Connection连接
conn = connect(host='localhost', port=3306, user='root', password='mysql', database='python1', charset='utf8')
# 得Cursor对象
cs = conn.cursor()
# 更新
# sql = 'update students set name="刘邦" where id=6'
# 删除
# sql = 'delete from students where id=6'
# 执行select语句，并返回受影响的行数：查询一条学生数据
sql = 'select id,name from students where id = 7'
# sql = 'SELECT id,name FROM students WHERE id = 7'
count=cs.execute(sql)
# 打印受影响的行数
print(count)