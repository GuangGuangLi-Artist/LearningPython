#coding=utf-8

import requests

def main():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    res = requests.get("http://www.baidu.com",headers=headers)
    con = res.content.decode("utf-8")
    print(con)


if __name__ == "__main__":
    main()
