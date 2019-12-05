#coding=utf-8


def set_level(level_num):
    def set_func(param):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("权限级别1")
            elif level_num == 2:
                print("权限级别2")
            return param()
        return call_func
    return set_func


@set_level(1)
def test1():
    print("---test1---")
    return "ok"


@set_level(2)
def test2():
    print("---test2---")
    return "ok2"


test1()
test2()




