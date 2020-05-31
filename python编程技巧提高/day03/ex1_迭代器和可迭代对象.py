#coding=utf-8

import requests
from collections import Iterable,Iterator

def get_weather(city):
    r = requests.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=13&tn=78040160_15_pg&wd=" + city)
    data = r.json()
    return data
if __name__ == '__main__':
    res = get_weather("王")
    print(res)