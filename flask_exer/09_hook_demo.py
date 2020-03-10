#coding=utf-8

from flask import Flask,current_app,redirect,url_for,session,request,g

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
@app.route("/login")
def login():
    print("index被执行")
    return "index page"

@app.before_first_request
def before_first_request():
    print("before_first_request被执行")

@app.before_request
def before_request():
    print("before_request被执行")


@app.after_request
def after_request(response):
    print("after_request被执行")
    return response

@app.teardown_request
def teardown_request(response):
    print("teardown_request被执行")
    return response




if __name__ == '__main__':
    app.run(debug=True)