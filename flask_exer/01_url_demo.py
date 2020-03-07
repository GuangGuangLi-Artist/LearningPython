#coding=utf-8

from flask import Flask,current_app,redirect,url_for

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
@app.route("/index")
def index():
    '''定义视图函数'''

    return  "hello flask"

@app.route('/post_only',methods=["POST"])
def post_only():
    return "post only page"


@app.route("/hello",methods=["GET"])
def hello():
    return "hello1"


@app.route("/hello",methods=["POST"])
def hello2():
    return "hello2"


@app.route("/h1")
@app.route("/h2")
def hi():
    return "hi"

@app.route("/login")
def login():
    #通过url_for函数，使用视图函数的名字找到对应的url地址
    url =url_for("index")
    return redirect(url)







if __name__ == '__main__':

    #查看flask的路由信息
    print(app.url_map)
    app.run(debug=True)