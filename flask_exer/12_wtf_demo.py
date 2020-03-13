#coding=utf-8

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
app = Flask(__name__)


'''定义表单的模型类'''
class RegisterForm(FlaskForm):
    #自定义注册表单模型类
    username = StringField()

@app.route("/login",methods=["POST"])
def login():
    return "login page"


if __name__ == '__main__':
    app.run(debug=True)
