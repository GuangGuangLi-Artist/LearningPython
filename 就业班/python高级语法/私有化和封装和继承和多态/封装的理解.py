#coding=utf-8

class T(object):
    def __init__(self,name):
        self.name = name

    def run(self):
        print(self.name + " is runing")

t = T("李广")

print(t.__class__)
print(t.__dict__)
t.run()

p = t.run()
print(p)


