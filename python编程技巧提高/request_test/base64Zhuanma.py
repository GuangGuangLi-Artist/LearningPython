#coding=utf-8


import base64
import requests

def run():

    list_a = []
    for i in range(1,101):
        bs = str(base64.b64encode(str(i).encode("utf-8")), "utf-8")
        list_a.append(bs)
    return list_a


def request_data():
    my_url = "https://renren.com/"
    my_header = {
        "Cookie":"",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    }
    res = run()
    my_formdata = {
        "appid":"x"
    }
    list_x = []
    for x in res:
        for key,value in my_formdata.items():
            my_formdata["appid"] = x
            list_x.append(my_formdata)
        return list_x

res_data = request_data()
print(res_data)




