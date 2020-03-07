#coding=utf-8

from flask import  request
from flask import Flask,abort,Response,make_response,jsonify
import json

app = Flask(__name__)

@app.route("/index",methods=["GET"])
def index():
    #json就是字符串
    data = {
        "name":"java",
        "age":"24"
    }

    #json.dumps(字典) 将python的字典转换为json字符串
    #json.loads(字符串) 将字符串转化为python的字典
    # json_str = json.dumps(data)
    # return json_str, 200,{"Content-Type":"application/json"}
    #jsonify帮助转化为json数据，并将响应头设置为"Content-Type":"application/json"
    return jsonify(city="nanjing",province="GS")


if __name__ == '__main__':
    app.run(debug=True)