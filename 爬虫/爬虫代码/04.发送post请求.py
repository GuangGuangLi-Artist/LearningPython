#coding=utf-8

import requests
import json
import sys


def main():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    fanyi_con = sys.argv[1]

    data = {
    "from": "zh",
    "to": "en",
    "query": fanyi_con,
    }

    url = "https://fanyi.baidu.com/basetrans"

    res = requests.post(url,data=data,headers=headers)
    con = res.content.decode()
    print(con)
if __name__ == "__main__":
    main()