#coding=utf-8

from flask import Flask,request
from flask_mail import Mail,Message
from flask_script import Manager,Shell
from threading import Thread
import os

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = "smtp.qq.com",
    MAIL_PORT= 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '940102569@qq.com',
    MAIL_PASSWORD = 'bhrylmalpnqebcbe'
)

mail = Mail(app)

@app.route("/")
def send_mail():
    msg = Message("测试邮件",sender="940102569@qq.com",recipients=["15607521232@163.com"])

    #邮件内容
    msg.body = "希望我这个邮件能够发送成功"

    #发送邮件
    mail.send(msg)
    print("mail send")
    return "send success"


if __name__ == '__main__':
    app.run(debug=True)