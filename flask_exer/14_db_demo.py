#coding=utf-8

from flask import Flask,render_template,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config():
    #SQLALCHEMY配置参数
    SQLALCHEMY_DATABASE_URI = 'mysql://liguang:123456@127.0.0.1:3306/liguang_test'

    #设置SQLALCHEMY自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

#创建数据库sqlalchemy工具对象
db =  SQLAlchemy(app)


#创建数据库模型类
class User(db.Model):
    '''用户表'''
    name =


class Role():
    pass

@app.route("/index")
def index():
    return


if __name__ == '__main__':
    app.run(debug=True)