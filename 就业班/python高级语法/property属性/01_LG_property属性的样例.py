#coding=utf-8

class Foo(object):

    @property
    def return_size(self):
        return 200


f = Foo()


n= f.return_size
print(n)