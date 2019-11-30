
def test2(a,b,*args,**kwargs):
    print("----" * 10)
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

    #test2(a,b,args,kwargs)相当于test2(1,2,(33,44),{'age': 18, 'name': '苏彪'})
    """
1
2
((33, 44), {'age': 18, 'name': '苏彪'})
{}


    #test2(a,b,*args,kwargs)#相当于test2(1,2,33,44,{'age': 18, 'name': '苏彪'})

1
2
(33, 44, {'age': 18, 'name': '苏彪'})
{}
"""
    test2(a, b, *args, **kwargs)#相当于test2(1,2,33,44,age=18,name="苏彪)

#test1(1,2,33,44,{"age":18},{"name":"苏彪"})
test1(1,2,33,44,age=18,name="苏彪")