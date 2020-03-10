#coding=utf-8

from flask import Flask,render_template

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
@app.route("/login")
def login():

    data = {
        "name":"subiao",
        "age":"25",
        "my_dict":{"city":"dingxi"},
        "my_list":[1,2,3,4,5,6],
        "my_int":0
    }
    return render_template("index.html",**data)

def li_step_2(li):
    '''自定义过滤器'''
    return li[::2]

#注册过滤器
app.add_template_filter(li_step_2,"li2")

@app.template_filter("li3")
def li_step_3(li):
    return li[::3]



if __name__ == '__main__':
    app.run(debug=True)