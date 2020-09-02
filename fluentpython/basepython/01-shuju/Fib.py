


a,b = 0,1
while a < 10:
    #关键字参数 end 可以用来取消输出后面的换行, 或使用另外一个字符串来结尾:
    print(a,end=",")
    a, b =b,a + b


#如果在循环内需要修改序列中的值（比如重复某些选中的元素），推荐你先拷贝一份副本。对序列进行循环不代表制作了一个副本进行操作。
# 切片操作使这件事非常简单：
words = ['cat','dag','fefenstrate']
for w in words[:]:
# for w in words:
    if len(w) > 6:
        words.insert(0,w)
        # words.remove(w)
print(words)

'''
range() 所返回的对象在许多方面表现得像一个列表，但实际上却并不是。此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，
这样就能节省空间。我们说这样的对象是 可迭代的 ，也就是说，适合作为函数和结构体的参数，这些函数和结构体期望在迭代结束之前可以从中获取连续
的元素。我们已经看到 for 语句就是这样一个迭代器。函数 list() 是另外一个；它从可迭代对象中创建列表。
'''
print(range(10))

print(list(range(10)))

'''
循环语句可能带有一个 else 子句；它会在循环遍历完列表 (使用 for) 或是在条件变为假 (使用 while) 的时候被执行，但是不会在循环被 break 语句终止时被执行
'''
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

#continue 语句也是借鉴自 C 语言，表示继续循环中的下一次迭代:
for number in range(2,10):
    if number % 2 == 0:
        print('Found an even number',number)
        #continue在条件成立时执行后就会继续下一次的迭代，不会再去执行条件外的代码
        continue
    print('Found a number',number)


