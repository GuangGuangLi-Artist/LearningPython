#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request,parse
from urllib import response

def request_get():
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"

    }
    url = 'https://m.douban.com/rexxar/api/v2/tv/35145271/verify_users?start=0&count=2&ck=aefV'
    req = request.Request(url=url,headers=headers,method='GET')
    res = request.urlopen(req)
    print("Status",res.status)

if __name__ == '__main__':
    request_get()