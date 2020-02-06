#coding=utf-8

import requests
from retrying import retry

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
@retry(stop_max_attempt_number=3)
def _parse_url(url,method,data,proxies):
    print("*" * 20)
    # respon = requests.get(url,headers=headers,timeout=3)
    if method=="POST":
        respon = requests.post(url,data=data,headers=headers,proxies=proxies)
    else:
        respon = requests.get(url,timeout=3,proxies=proxies)

    assert respon.status_code == 200
    return respon.content.decode()


def parse_url(url,method="GET",data=None,proxies={}):
    try:
        html_str = _parse_url(url,method,data,proxies)
    except:
        html_str = None

    return html_str

if __name__ == "__main__":
    url = "www.baidu.com"
    print(parse_url(url))