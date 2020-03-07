#coding=utf-8

from flask import  request
from flask import Flask,abort,Response
import json

app = Flask(__name__)

@app.route("/login",methods=["GET"])
def login():
    # name = request.form.get()
    # pwd = request.form.get()
    name = ""
    pwd  = ""
    if name != "zhangsan" or pwd != "admin":

        #使用abort函数可以立即终止视图函数的执行
        #并可以返回给前端特点的信息
        #1.传递状态码信息，必须是标准的http状态码
        abort(404)
        # resp = Response("login filed")
        # abort(resp)
    return "login success"
@app.errorhandler(404)
def handle_404(err_msg):
    '''自定义错误处理方法'''

    return "err_msg内容是:%s" % err_msg


if __name__ == '__main__':
    app.run(debug=True)