#coding=utf-8


class Foo(object):

    def get_bar(self):
        return "李广广"

    bar = property(get_bar)

obj = Foo()
t = obj.bar
print(t)