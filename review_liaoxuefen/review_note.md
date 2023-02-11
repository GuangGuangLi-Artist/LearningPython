### 使用枚举类
    Python 提供了Enum类来实现这个功能
### 使用元类
    type():动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
    要创建一个class对象，type()函数依次传入三个参数:
        1. class的名称
        2. 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法
        3. class 的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名hello 上。

```python
def fn(self,name='wprld'):
    print('Hello, %s' %(name))

Hello = type('Hello',(object,),dict(hello=fn))
```

### 错误、调试和测试
#### 错误处理
    raise 是自定义的抛出的错误
```python
try:
    print('tyr')
    res = 10 / 0
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
    raise '---'
finally:
    print('finally')
```

#### 调试
1. 断言 assert
2. logging
3. pdb

### IO编程
#### 文件读写
1. 读文件
    * 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用 read(size)比较保险；如果是配置文件，调用 readlines()最方便
2. 二进制文件
   * 用'rb'模式打开文件即可
3. 字符编码 
    * 要读取非 UTF-8 编码的文本文件，需要给 open()函数传入 encoding 参数 例如，读取 GBK 编码的文件：f = open('gbk.txt', 'r', encoding='gbk')
4. 写文件
   * 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#### StringIO 和 BytesIO
    很多时候，数据读写不一定是文件，也可以在内存中读写,StringIO 顾名思义就是在内存中读写 str 要把 str 写入 StringIO，我们需要先创建一个 StringIO，然后，像文件一
    样写入即可 getvalue()方法用于获得写入后的 str。
    BytesIO 实现了在内存中读写 bytes，我们创建一个 BytesIO，然后写入一些 bytes：
#### 操作文件和目录
   os模块
   1. os.name 操作系统类型
   2. os.environ 环境变量
#### 序列化
   1. 我们把变量从内存中变成可存储或传输的过程称之为序列化
   2. 把变量内容从序列化的对象重新读到内存里称之为反序列化
   3. Python 提供了 pickle 模块来实现序列化
   4. dumps()方法返回一个 str，内容就是标准的 JSON。类似的，dump()方法 可以直接把 JSON 写入一个 file-like Object
   5. 把 JSON 反序列化为 Python 对象，用 loads()或者对应的 load()方法， 前者把 JSON 的字符串反序列化，后者从 file-like Object 中读取字符 串并反序列化
