# -*-coding:utf-8 -*-

"""第五章 数据结构

1.列表详解
    列表推导式
    嵌套的列表推导式
2.元组和序列
3.字典和集合
"""

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







if __name__ == '__main__':
    list_demo = List_Demo()
    list_demo.operate_list(list_demo.fruits)
    print("*" * 50)
    list_demo.list_to_stack()
    print("*" * 50)
