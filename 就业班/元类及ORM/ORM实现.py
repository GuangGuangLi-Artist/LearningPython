#coding=utf-8

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        mappings = dict()

        for k,v in attrs.items():
            if isinstance(v,tuple):
                print('Found mapping: %s ==> %s ' %(k,v))
                mappings[k] = v


        for k in mappings.keys():
            attrs.pop(k)


        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return  type.__new__(cls,name,bases,attrs)

class Model(object,metaclass=ModelMetaclass):
    def __init__(self,**kwargs):
        for name,value in kwargs.items():
            setattr(self,name,value)


    def save(self):
        files = []
        args = []
        for k,v in self.__mappings__.items():
            files.append(v[0])
            args.append(getattr(self,k,None))


        args_temp = list()
        for temp in args:
            if isinstance(temp,int):
                args_temp.append(str(temp))
            elif isinstance(temp,str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s)' %(self.__table__,','.join(files),','.join(args_temp))
        print('SQL:%s' % sql)

class User(Model):
    uid = ('uid',"int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

u = User(uid=12345,name='Michael', email='test@orm.org', password='my-pwd')
u.save()
