#coding=utf-8

from flask import  request
from flask import Flask,abort,Response,make_response,jsonify
import json

app = Flask(__name__)

@app.route("/setcookie",methods=["GET"])
def setCookie():

    #设置cookie
    resp = make_response("success")
    resp.set_cookie("name","su")
    resp.set_cookie("age","22",max_age=3600)
    resp.headers["Set-Cookie"] = "age=28; Expires=Sat, 07-Mar-2020 16:36:35 GMT; Max-Age=3600; Path=/"
    return  resp


@app.route("/getcookie")
def getcookie():
    c = request.cookies.get("name")
    return c


@app.route("/delecookie")
def deletecookie():
    resp = make_response("dele success")
    resp.delete_cookie("name")
    return resp



if __name__ == '__main__':
    app.run(debug=True)