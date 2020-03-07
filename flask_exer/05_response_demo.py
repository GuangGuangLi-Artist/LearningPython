#coding=utf-8

from flask import  request
from flask import Flask,abort,Response,make_response
import json

app = Flask(__name__)

@app.route("/index",methods=["GET"])
def index():

    #1.使用元组返回自定义的响应信息
    #.响应体   状态码  响应头
    # return ("login success", 400, [("liguang","haha"),("city","shanghai")])
    # return ("login success", 666, {"name":"liguang", "city": "shenzheng"})
    # return ("login success", "666 self dingyi", {"name": "liguang", "city": "shenzheng"})


    #2.使用make_response来构造响应体

    resp = make_response("index page")
    resp.status = "999 liguang"
    resp.headers["city"] = "SZ"
    return resp


if __name__ == '__main__':
    app.run(debug=True)