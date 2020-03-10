#coding=utf-8

from flask import Flask,current_app,redirect,url_for,session,request,g
from flask_script import Manager

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
manage = Manager(app)
@app.route("/login")
def login():
    return "login success"


if __name__ == '__main__':
    manage.run()