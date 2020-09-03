'''
创建函数有三种设置参数的方式
1：默认参数--是在函数定义的时候就已经写好的，如def fun(name="li")
2：关键字参数 是在函数调用的时候传递的键值对，如ask(prompt="haha")
3：位置参数
其中，需要注意的是
1：默认参数必须指向不可变对象
2：必填参数在前，默认参数在后

'''

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
if __name__ == '__main__':
    ask_ok('Do you really want to quit?')