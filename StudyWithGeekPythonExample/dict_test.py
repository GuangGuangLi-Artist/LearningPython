#coding=utf-8

def fmap(a,b):
    return a,b

a_str = '1,2,3,4,5,6'
b_str = 'a,b,c,d,e,f'
arr_a = a_str.split(',')
arr_b = b_str.split(',')


c_di = map(fmap,arr_a,arr_b)
c_dict = dict(c_di)
print(c_dict)