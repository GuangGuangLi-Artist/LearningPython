#coding=utf-8

from flask import Flask,current_app,redirect,url_for,session,request,g

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
app.config["SECRET_KEY"] = "djsajjasljdlkasjlkd"
@app.route("/login")
def login():
    '''定义视图函数'''
    session["name"] = "python"
    session["age"] = "12345678901"
    say_hello()
    g.username = "subiao"
    return  "hello login success"


def say_hello():
    username = g.username
    return username

@app.route("/getsession")
def get_seeeion():
    name = session.get("name")
    return "hello %s " % name

if __name__ == '__main__':
    app.run(debug=True)