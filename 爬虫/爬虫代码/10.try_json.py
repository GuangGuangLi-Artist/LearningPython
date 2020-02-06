#coding=utf-8


import requests
from parse_url import parse_url
import json
from pprint import pprint




def main():
    url = "http://127.0.0.1:8000/return_json"
    html_str = parse_url(url)

    ret1 = json.loads(html_str)
    # pprint(ret1)


    # with open("douban.json","w",encoding="utf-8") as f:
    #     f.write(json.dumps(ret1,ensure_ascii=False,indent=2))
    #
    # with open("douban.json","r",encoding="utf-8") as f:
    #     ret2 = f.read()
    #     ret3 = json.loads(ret2)
    #     print(ret3)


    #使用json,load提取类文件对象中的数据
    with open("douban.json","r",encoding="utf-8") as f:
        ret4 = json.load(f)
        print(ret4)
        print(type(ret4))

    # 使用json,dump能够把python类型放入类文件对象中
    with open("douban1.json","w",encoding="utf-8") as f:
        json.dump(ret1,f,ensure_ascii=False,indent=2)

if __name__ == "__main__":
    main()