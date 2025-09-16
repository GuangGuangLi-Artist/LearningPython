# -*-coding:utf-8 -*-

"""第五章 数据结构

1.列表详解
    列表推导式
    嵌套的列表推导式
2.元组和序列
3.字典和集合
"""

from collections import deque
import math

class List_Demo:
    
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    
    def operate_list(self,fruits):
        print(fruits.count('apple')) #统计某个元素出现的次数
        print("fruits index后查找banana",fruits.index('banana')) #从左到右找某个元素第一次出现的索引位置
        print("fruits index 4后查找banana",fruits.index('banana',4)) #从索引4开始找某个元素第一次出现的索引位置
        fruits.reverse() #反转列表
        print("fruits reverse后",fruits)
        fruits.append('grape') #在列表末尾添加新元素
        print("fruits append到末尾后",fruits)
        fruits.sort() #对列表进行排序
        print("fruits sort后",fruits) #默认按字母顺序排序
        fruits.pop() #移除并返回列表末尾的元素
        print("fruits pop末尾元素后",fruits)
        fruits.remove('banana') #移除列表中某个值的第一个匹配项
        print("fruits remove第一个banana后",fruits)
        fruits.insert(2,'watermelon') #在指定位置插入元素
        print("fruits insert到索引2位置后",fruits)
        fruits.extend(['mango','coconut']) #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        print("fruits extend多个元素后",fruits)
        acp = fruits.copy() #浅复制列表
        print("fruits copy后",acp)
        fruits.clear() #清空列表
        print("fruits clear后",fruits)
        print("acp",acp)
    
    #用列表实现堆栈
    def list_to_stack(self):
        stack = [3,4,5]
        print("stack 开始使用append()末尾添加元素")
        stack.append(6)
        stack.append(7)
        print("stack",stack)
        print("stack pop",stack.pop())
        print("stack pop",stack.pop())
        print("stack after pop",stack)


    #用列表实现队列
    def list_to_deque(self):
        queue = deque(['Eric','John','Michael'])
        print("queue",queue)
        queue.append('Terry') #在队列的右侧添加元素
        queue.append('Graham')
        print("queue append",queue)
        print("queue popleft",queue.popleft()) #从队列的左侧移除并返回一个元素
        print("queue after popleft",queue)

    #列表推导式
    def list_comprehensions(self):
        squares = list(map(lambda x: x**2, range(10))) #使用map和lambda函数生成平方数列表
        print("squares",squares)
        #列表推导式实现
        squares_comp = [x**2 for x in range(10)]
        print("squares_comp",squares_comp)
        vec = [2,4,6]
        print([3*x for x in vec]) #对列表中的每个元素进行操作
        print([3*x for x in vec if x > 3]) #对列表中满足条件的元素进行操作
        print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]) #使用两个for循环嵌套
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        print("matrix",matrix)
        print([row[0] for row in matrix]) #提取矩阵的第一列
        print([row[1] for row in matrix]) #提取矩阵的第二列
        print([row[2] for row in matrix]) #提取矩阵的第三列
        print([[row[i] for row in matrix] for i in range(3)]) #转置矩阵

        vec = [-4,-2,0,2,4]
        print([x*2 for x in vec]) #对列表中的每个元素进行操作
        print([x for x in vec if x >= 0]) #对列表中满足条件的元素进行操作
        print([abs(x) for x in vec]) #对列表中的每个元素进行操作
        freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
        print([weapon.strip() for weapon in freshfruit]) #对列表中的每个元素进行操作
        print([(x, x**2) for x in range(6)]) #生成元组列表
        #使用两个for循环展开嵌套的列表
        vec_1 = [[1,2,3], [4,5,6], [7,8,9]]
        print([num for elem in vec_1 for num in elem])

    #del语句
    def del_statement(self):
        a = [-1,1,66.25,333,333,1234.5]
        print("a",a)
        del a[0] #删除索引为0的元素
        print("del a[0]",a)
        del a[2:4] #删除索引2到4之间的元素
        print("del a[2:4]",a)
        del a[:] #清空列表
        print("del a[:]",a)
        del a #删除整个列表
        #print(a) #会报错

    #元组和序列
    #元组
    def tuple_demo(self):
        t = 12345,54321,'hello!' #创建元组
        print("t",t)
        print(t[0]) #访问元组中的元素
        print(t) #打印整个元组
        u = t,(1,2,3,4,5) #嵌套元组
        print("u",u)
        empty = () #创建空元组
        singleton = 'hello', #创建只有一个元素的元组，必须在元素后面加逗号
        print("len(empty)",len(empty))
        print("len(singleton)",len(singleton))
        print("singleton",singleton)
        print("singleton[0]",singleton[0])
        v = ([1,2,3],[3,2,1]) #元组中可以包含可变对象
        print("v",v)
        #元组不可变，所以没有append、remove等方法，但可以对包含的可变对象进行修改
        v[0].append(4)
        print("v after append",v)

        tt = 12345,54321,'hello!'
        x,y,z = tt #序列解包
        print("序列解包:","x",x,"y",y,"z",z)

    #集合
    def set_demo(self):
        basket = {'apple','orange','apple','pear','orange','banana'}
        print("basket",basket) #重复的元素会被自动去重
        print('orange in basket is','orange' in basket) #成员测试
        print('crabgrass in basket is','crabgrass' in basket) #成员测试      
        a = set('abracadabra') #创建集合
        b = set('alacazam') #创建集合
        print("a",a)        
        print("b",b)
        print("a - b",a - b) #a中有而b中没有的元素
        print("a | b",a | b) #a和b中所有的元素          
        print("a & b",a & b) #a和b中都有的元素
        print("a ^ b",a ^ b) #在a或b中但不同时在a和b中的元素

        sa = {x for x in 'abracadabra' if x not in 'abc'} #集合推导式
        print("sa",sa)

    # 字典
    def dict_demo(self):
        tel = {'jack':4098,'sape':4139}
        tel['guido'] = 4127 #添加键-值对
        print("tel",tel)
        print("tel['jack']",tel['jack']) #通过键访问值
        del tel['sape'] #删除键-值对
        print("tel after del",tel)  
        print("tel.keys()",list(tel.keys())) #获取所有的键
        print("tel.values()",list(tel.values())) #获取所有的值  
        print("tel.items()",list(tel.items())) #获取所有的键-值对
        tel2 = dict([('sape',4139),('guido',4127)]) #通过键-值对列表创建字典
        print("tel2",tel2)
        tel3 = dict(sape=4139,guido=4127,jack=4098) #通过关键字参数创建字典
        print("tel3",tel3)
        print("guido in tel3 is",'guido' in tel3) #成员测试
        print("len(tel3)",len(tel3)) #字典长度
        for k,v in tel3.items(): #遍历字典
            print(k,v)
        for k in tel3: #遍历字典的键
            print(k)    
        for v in tel3.values(): #遍历字典的值
            print(v)
        tel3_copy = tel3.copy() #浅复制字典
        print("tel3_copy",tel3_copy)
        dict_comp = {x: x**2 for x in (2,4,6)} #字典推导式
        print("dict_comp",dict_comp)
    
    #循环的技巧
    def loop_tricks_items(self):
        knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        print("items()",knights.items())
        for k,v in knights.items(): #同时解包键-值对
            print(k,v)
    def loop_tricks_enumerate(self):
        for i,v in enumerate(['tic','tac','toe']): #同时获取索引和值
            print(i,v)

    def loop_tricks_zip(self):
        questions = ['name','quest','favorite color']
        answers = ['lancelot','the holy grail','blue']
        for q,a in zip(questions,answers): #并行迭代多个序列
            print('What is your {0}? It is {1}.'.format(q,a))
    def loop_tricks_revered(self):
        for i in reversed(range(1,10,2)): #反向迭代
            print(i)
    def loop_tricks_sorted(self):
        basket = ['apple','orange','apple','pear','orange','banana']
        for f in sorted(set(basket)): #按顺序迭代
            print(f)
    def loop_tricks_sor_set(self):
        basket = ['apple','orange','apple','pear','orange','banana']
        for f in sorted(set(basket),key=len): #按长度排序后迭代
            print(f)
    
    #在循环中修改列表的内容时，创建新列表比较简单，且安全
    def loop_update_List(self):
        raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
        filtered_data = []
        for value in raw_data:
            if not math.isnan(value):
                filtered_data.append(value)
        
        print("filtered_data",filtered_data)

    def loop_tricks(self):
        self.loop_tricks_items()
        print("-" * 20)
        self.loop_tricks_enumerate()
        print("-" * 20)
        self.loop_tricks_zip()
        print("-" * 20)
        self.loop_tricks_revered()
        print("-" * 20)
        self.loop_tricks_sorted()
        print("-" * 20)
        self.loop_tricks_sor_set()
        print("-" * 20)
        self.loop_update_List()





        

    







if __name__ == '__main__':
    list_demo = List_Demo()
    list_demo.operate_list(list_demo.fruits)
    print("*" * 50)
    list_demo.list_to_stack()
    print("*" * 50)
    list_demo.list_to_deque()
    print("*" * 50)
    list_demo.list_comprehensions()
    print("*" * 50)
    list_demo.del_statement()
    print("*" * 50)
    list_demo.tuple_demo()
    print("*" * 50)
    list_demo.set_demo()
    print("*" * 50)
    list_demo.dict_demo()
    print("*" * 50)
    list_demo.loop_tricks()
    print("*" * 50)
