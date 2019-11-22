#coding=utf-8

import re


def main():
    email = input("请输入你的邮箱地址:")
    ret = re.match(r"^[a-zA-Z0-9]{4,20}@163\.com$",email)
    if ret:
        print("%s 地址符合邮箱格式要求" % (email))
    else:
        print("%s 地址不符合邮箱格式要求" % (email))


if __name__ == "__main__":
    main()

