#coding=utf-8

from flask import Flask,render_template,flash

app = Flask(__name__)
app.config["SECRET_KEY"]="adafdfafa"
flag = True
@app.route("/index")
def index():
    if flag:
        # 添加闪现信息
        flash("hello1")
        flash("hello2")
        flash("hello3")
        global flag
        flag = False

    return render_template("macro.html")


if __name__ == '__main__':
    app.run(debug=True)