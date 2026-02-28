# -*- coding: utf-8 -*-
# @Time    : 2024/6/11 17:28
# @Author  : guangli
# @File    : pythonInterview.py
# @Software: vscode

<<<<<<< HEAD
# 1. 在python中如何实现单例模式？
# 单例模式是指让一个类只能创建唯一的实例 实现单例模式有两种常见方法，第一个方式是使用装饰器，第二种方式是使用元类。
# 方式一：使用装饰器

from functools import wraps

def singleong(cls):
    """单例累装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return wrapper

@singleong
class MyClass:
    pass

# 方式二：使用元类
class singletonMeta(type):
    """"自定义单例元类"""

    def __init__(cls,*args,**kwargs):
        cls.__instance = None
        super().__init__(*args,**kwargs)

    def __call__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args,**kwargs)
        return cls.__instance
    
class president(metaclass =singletonMeta):
    pass

# 闭包和装饰器
# 闭包内层函数使用了外层函数的变量，并且外层函数把这个内层函数给返回了
# 闭包的三个条件
 #1.函数嵌套：在一个函数里定义另一个函数
 #2.内部函数引用外部变量：里面的函数要用到外面函数的变量
 #3.外部函数返回内部函数：外面的函数要把里面的函数作为结果返回

def outer(x):# 外层函数，带参数 x
    def inner(y): # 内层函数
        return x + y # inner 使用了 outer 的变量 x (这就是闭包的关键！)
    return inner  # outer 返回了 inner (注意：不是 inner())

add_5 = outer(5) # add_5 是一个函数，它记住了 x=5。
print(add_5(10)) #这就是闭包的威力：它把数据（x的值）和操作（inner函数）封装在了一起。

print("*" * 20)

# 装饰器
# 装饰器是一个函数，它接受另一个函数作为参数，并返回一个新的函数。装饰器通常用于在不修改原函数代码的情况下，增强或改变函数的行为。
# 第一类 无参装饰器
def no_args_decorator(func):
    def wrapper():
        print("在函数执行之前：我先点个外卖")
        func() # 执行原函数
        print("在函数执行之后：我洗个碗")
    return wrapper

@no_args_decorator
def say_hello():
    print("这是我的函数，正在执行...")


say_hello() # 调用被装饰的函数
print("*" * 20)

# 第二类 带参装饰器(三层函数)
def with_args_decorator(times):# 第一层：接收装饰器的参数
    def decorator(func):# 第二层：接收函数
        def wrapper(*args,**kwargs):# # 第三层：执行逻辑
            for _ in range(times):
                result = func(*args,**kwargs) # 执行原函数
            return result
        return wrapper
    return decorator

@with_args_decorator(3) # 这里传入装饰器参数
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # 调用被装饰的函数
print("*" * 20)
# 第三类 类装饰器 使用类的实例来充当装饰器，通常利用 __call__ 方法
class CountCalls:
    def __init__(self,func):
        self.func = func
        self.count = 0

    def __call__(self,*args,**kwargs):# 让实例像函数一样被调用
        self.count += 1
        print(f"函数调用了 {self.count} 次")
        return self.func(*args,**kwargs)

@CountCalls #现在的 say_hi 已经不再是原来的函数了，它变成了一个 MyDecorator 类的实例（对象）
def say_hi():
    print("Hi!")

say_hi()
say_hi()
print("*" * 20)

# __call__ 方法的作用是让一个对象能够像函数一样被调用。当你在一个对象上使用括号（例如 obj()）时，Python 会自动调用该对象的 __call__ 方法。这使得类装饰器非常强大，因为它们可以在不修改原函数代码的情况下，增强或改变函数的行为。
class Robot:
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print(f"Hello, I am {self.name} the Robot!")
r1 = Robot("R2-D2")
r1() # 这会调用 r1 的 __call__ 方法，输出：Hello, I am R2-D2 the Robot!

print("*" * 20)
# __call__ 方法什么时候用 ？
#当你需要一个东西，它调用起来像函数（obj()），但又需要记住一些数据（self.xxx）的时候。

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"Count is now {self.count}")
counter = Counter()
counter() # Count is now 1  
counter() # Count is now 2
counter() # Count is now 3
print("*" * 20)

# 2.不适用中间变量。交换两个变量a,b的值

# 方法一：异或
a = 5
b = 10
print(f"交换前：a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"交换后：a={a}, b={b}") # 输出：10 5
print("*" * 20)
# 方法二：加减  
a = 5
b = 10
print(f"交换前：a={a}, b={b}")
a = a + b
b = a - b
a = a - b
print(f"交换后：a={a}, b={b}") # 输出：10 5
print
# 方法三：拆包
a = 5
b = 10
print(f"交换前：a={a}, b={b}")
a, b = b, a
print(f"交换后：a={a}, b={b}") # 输出：10 5
print("*" * 20)

# 3.写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变。

def dedup(items):
    result = []
    seen = set()
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
# 测试
my_list = [1, 2, 3, 2, 4, 1, 5]
print(dedup(my_list)) # 输出：[1, 2, 3, 4, 5]
print("*" * 20)
#改造成生成器
def dedup_generator(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            
# 测试
my_list = [1, 2, 3, 2, 4, 1, 5]
gebenator = dedup_generator(my_list)
print(list(gebenator))
print("*" * 20)

# 5 Lambda函数是什么，举例说明的它的应用场景。
"""Lambda函数也叫匿名函数，它是功能简单用一行代码就能实现的小型函数。
Python中的Lambda函数只能写一个表达式，这个表达式的执行结果就是函数的返回值，
不用写`return`关键字。Lambda函数因为没有名字，
所以也不会跟其他函数发生命名冲突的问题。
主要的作用是通过向函数传入函数或让函数返回函数最终实现代码的解耦合"""
# 列表筛选出奇数并进行平方
numbers = [12,5,7,10,8,19]
nums_lambda = list(map(lambda x:x ** 2,filter(lambda x:x % 2 != 0,numbers)))
print(nums_lambda) # 输出：[25, 49, 361]
#列表生成式实现
gen_numbers = [x ** 2 for x in numbers if x % 2 != 0]
print(gen_numbers) # 输出：[25, 49, 361]

# 深拷贝浅拷贝
=======
# 1. Python中的数据类型有哪些？请简要说明每种数据类型的特点。
# Python中的数据类型主要包括以下几种：
# - 数字类型（int、float、complex）：用于表示整数、浮点数和复数。
# - 字符串类型（str）：用于表示文本数据，支持单引号、双引号和三引号。
# - 列表类型（list）：用于存储有序的可变集合，可以包含不同类型的元素。  
# - 元组类型（tuple）：用于存储有序的不可变集合，可以包含不同类型的元素。
# - 集合类型（set）：用于存储无序的唯一元素集合，支持数学集合操作。
# - 字典类型（dict）：用于存储键值对的无序集合，键必须是不可变类型，值可以是任意类型。
# - 布尔类型（bool）：用于表示真（True）和假（False     ）两种状态。
# - None类型：用于表示空值或无值的特殊类型。    
# 2. Python中的列表和元组有什么区别？请举例说明。
# 列表（list）和元组（tuple）是Python中两种常用的数据结构，它们的主要区别在于可变性和使用场景：
# - 可变性：列表是可变的，可以修改、添加或删除元素；
#   元组是不可变的，一旦创建就不能修改。
# - 使用场景：列表适用于需要频繁修改数据的场景，而元组适用于需要保护数据不被修改的场景。
# 例如：
# 列表示例：
my_list = [1, 2, 3]
my_list.append(4)  # 列表可以修改
print(my_list)  # 输出: [1, 2, 3, 4]    
# 元组示例：
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # 元组不能修改，会抛出AttributeError
print(my_tuple)  # 输出: (1, 2, 3)
# 3. Python中的字典是什么？请举例说明如何使用字典。
# 字典（dict）是Python中的一种数据结构，用于存储键值对。每个键必须是唯一的，并且必须是不可变类型（如字符串、数字或元组）。字典的值可以是任意类型。
# 字典使用花括号{}定义，键值对之间用冒号:分隔，多个键值对之间用逗号,分隔。
# 例如：
my_dict = { "name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # 输出: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 访问字典中的值
print(my_dict["name"])  # 输出: Alice   
# 添加或修改字典中的键值对
my_dict["age"] = 31  # 修改已有键的值
my_dict["country"] = "USA"  # 添加新的键值对
>>>>>>> d4d4ba71d940abc24566dd4e781796e4181051e2
