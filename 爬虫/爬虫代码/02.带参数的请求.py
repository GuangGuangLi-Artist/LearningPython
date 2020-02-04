#coding=utf-8

import requests

def main():
    # headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    # kw = {"kw":"武汉肺炎"}
    # url = "http://www.baidu.com/s?"
    # res = requests.get(url,headers=headers,params=kw)
    # con = res.content.decode("utf-8")
    # print(res.status_code)
    # print(con)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    kw = {"kw": "武汉肺炎"}
    #请注意这里的format方法
    url = "http://www.baidu.com/s?wd={}".format("李广")
    res = requests.get(url, headers=headers)
    con = res.content.decode("utf-8")
    print(res.status_code)
    print(con)





if __name__ == "__main__":
    main()