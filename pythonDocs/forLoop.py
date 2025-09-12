# 创建示例多项集
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


def print_users(users):
    for user, status in users.items():
        print(f'{user}: {status}')


def print_test(num):
    print(num % 2)
    for i in range(2, num):
        print(i)
def loop_else(num):
    for n in range(2,num):
        for x in range(2,n):
            if n % x == 0:
                print(f'{n} equals {x} * {n//x}')
                break
        else:
            print(f'{n} is a prime number')

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _: #“变量名” _ 被作为 通配符 并必定会匹配成功
            return "Something's wrong with the internet"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def where_is(point):
        match point:
            case (0, 0):
                print("Origin")
            case (0, y):
                print(f"Y={y}")
            case (x, 0):
                print(f"X={x}")
            case (x, y):
                print(f"X={x}, Y={y}")
            case _:
                raise ValueError("Not a point")

class FuncDemo:
    def standard_args(self, arg):
        print(arg)


    def pos_only_arg(self, arg, /):#仅限使用位置形参
        print(arg)
    def keyword_only_arg(self, *, arg):#只允许关键字参数
        print(arg)

    
    def combined_example(self,pos_only,/,standard,*,kw_only):
        print(pos_only,standard,kw_only)

    """
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        1.使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，或同时接收位置形参和关键字时，这种方式很有用。
        2.当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字。
        3.对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动。
    """


    def foo(self,name, **kwds):
        return 'name' in kwds
    
    def bar(self,name, /, **kwds):
        return 'name' in kwds
    
    #任意实参
    def contactString(self, *args, sep="/"):
        return sep.join(args)
    
    def contactString2(self, *args,**kwargs):
        sep = kwargs.get("sep","/")
        return sep.join(args)
    
    #解包实参 *
    def demo_unpack1(self, arg=[3,6]):
        return list(range(*arg)) #等同于list(range(3,6))
    #解包实参 **    
    def parrot(self,voltage,state="a stiff",action="voom"):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", state)


    # lambda表达式 Lambda 函数可用于任何需要函数对象的地方
    #使用方式1 使用lambda表达式返回函数
    def make_incrementor(n):
        return lambda x: x + n
    
    #使用方式2 作为内置函数的参数
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    
    


if __name__ == '__main__':
    #print_users(users)
    # print_test(2)
    # loop_else(10)
    # print(http_error(500))
    Point.where_is((5,5))
    Point.where_is((0,0))
    print("*" * 50)

    demo = FuncDemo()
    demo.standard_args(2)
    demo.standard_args(arg=22)
    demo.pos_only_arg(1)
    #demo.pos_only_arg(arg=1) #报错#TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
    demo.keyword_only_arg(arg=3)
    #demo.keyword_only_arg(3) #报错#TypeError: keyword_only_arg() takes 0 positional arguments but 1 was given
    demo.combined_example(1,standard=2,kw_only=3)
    demo.combined_example(1,2,kw_only=3)
    #demo.combined_example(1,2,3) #报错#TypeError: combined_example() missing 1 required keyword-only argument: 'kw_only'
    print("*" * 50)
    try:
        res = demo.foo(1,**{'name':2}) #FuncDemo.foo() got multiple values for argument 'name'
        print(res)
    except Exception as e:
        print(e)

    res1 =  demo.bar(1,**{"name":2}) #True
    print(res1)
    print("*" * 50)
    print(demo.contactString("earth","mars","venus"))
    print(demo.contactString("earth","mars","venus",sep="*"))
    print(demo.contactString2("earth","mars","venus"))
    print(demo.contactString2("earth","mars","venus",sep="*"))
    print("*" * 50)
    print(demo.demo_unpack1(arg=[3,7]))
    parrot_user = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    demo.parrot(**parrot_user)
    print("*" * 50)

    mi = FuncDemo.make_incrementor(42)
    print(mi(1))
    print("*" * 50)
    print(demo.pairs)
    print("*" * 50)
    
    
