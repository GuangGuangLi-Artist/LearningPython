#coding=utf-8

from flask import Flask,current_app,redirect,url_for,request,jsonify
# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
@app.route("/login",methods=["POST"])
def login():
    #接受参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    #参数判断
    if not all([user_name,password]):
        resp = {
            "code":400,
            "msg":"invaild param"
        }
        return jsonify(resp)

    elif user_name == "admin" and password == "python":
        resp = {
            "code": 200,
            "msg": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 500,
            "msg": "wrong username or password"
        }
        return jsonify(resp)







if __name__ == '__main__':
    app.run(debug=True)