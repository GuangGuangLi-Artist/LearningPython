# -*- coding:utf-8 -*-

'''
filter()函数用于过滤序列
    接收一个函数和一个序列，把函数作用于序列的每个函数，然后根据返回值是True和False决定是否保留元素
'''
def is_odd(n):
    if n % 2 == 1:
        return n
    
list_odd = filter(is_odd,list(range(1,11)))
print(list(list_odd))

#用filter求素数
#生成器生成奇数序列
def __odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#筛选函数
def __not_divisiable(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = __odd_iter() #初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(__not_divisiable(n),it) #构造新序列


# primes()是一个无无限序列，设置一个退出循环的条件
prime_list = []
for i in primes():
    if i < 100:
        prime_list.append(i)
    else:
        break

print(prime_list)

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    #return str(n) == str(n)[::-1]
    return str(n) == ''.join(reversed(str(n)))

print(list(filter(is_palindrome,range(1,102))))

print('-------------')
#排序 排序的核心是比较两个元素的大小 sorted()可以接受一个key来实现自定义的排序

list_no = ['bob', 'about', 'Zoo', 'Credit']
list_afterno = sorted(list_no,key=str.lower,reverse=True)
print(list_afterno)

#假设我们用一组tuple表示学生名字和成绩： L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] 请用sorted()对上述列表分别按名字排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
        return t[0].lower()

L_name = sorted(L,key = by_name)
print (L_name)
#按照成绩从高到底
def by_score(t):
    return t[1]

print(sorted(L_name,key=by_score,reverse=True))
