#coding=utf-8

import re


def main():
    names = ["age","__age","1age","age1","a_age","age_1_2","age!","a#ge123","-----","______"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$",name)
        if ret:
            print("变量名:%s 符合要求>>>正则匹配到的结果是：%s" %(name,ret.group()))
        else:
            print("变量名:%s 不符合要求" % (name))


if __name__ == "__main__":
    main()