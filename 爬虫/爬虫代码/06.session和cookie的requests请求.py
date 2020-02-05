#coding=utf-8

import requests



def main():
    session = requests.session()
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"940102569@qq.com",
        "password":"930819l@g"
    }

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}





    #使用session发送post请求，cookie保存在其中
    session.post(url,headers=headers,data=data)
    con = session.get("http://www.renren.com/526950701/profile",headers=headers)


    #保存页面
    with open("renren.html","w",encoding="utf-8") as file:
        file.write(con.content.decode())

if __name__ == "__main__":
    main()