#coding=utf-8

from flask import  request
from flask import Flask
import json

app = Flask(__name__)

@app.route("/index",methods=["POST","GET"])
def index():

    #request中包含了所有从前端发送过来的数据，通过request.form可以提取请求体中的表单格式的数据，是一个类字典的对象
    name = request.form.get("name")
    age = request.form.get("age")
    name_li = request.form.getlist("name")
    # print(request.data)
    # print(json.dumps(request.form))
    # print(request.form)
    city = request.args.get("city")
    return "hello name=%s,age=%s,city=%s,name_li=%s" %(name,age,city,name_li)


@app.route("/upload",methods=["POST"])
def up_load():
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "未上传文件"

    #将文件保存到本地
    # with open("./pic.png", "wb") as f:
    #     data = file_obj.read()
    #     f.write(data)
    file_obj.save("1.png")
    return "上传成功"
if __name__ == '__main__':
    app.run(debug=True)