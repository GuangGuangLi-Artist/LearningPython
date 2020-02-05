#coding=utf-8

import requests



def main():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    proxy = {"http":"171.11.33.139:40318"}



    url = "http://www.baidu.com"

    res = requests.get(url,headers=headers,proxies=proxy)
    con = res.content.decode()
    print(con)
if __name__ == "__main__":
    main()