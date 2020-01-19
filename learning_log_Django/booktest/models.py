from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=128,unique=True,db_column='title',db_index=True)
    #btitle = models.CharField(max_length=128, unique=True,  db_index=True)
    #价格最大位数为10，小数位数为2
    #bprince = models.DecimalField(max_digits=10,decimal_places=2)
    bpub_date = models.DateField(auto_now_add=True)
    bread = models.ImageField(default=0)
    bcomment = models.ImageField(default=0,null=True,blank=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=128)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=256,null=True,blank=True)
    #一对多的关系
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)


    def __str__(self):
        return self.hname
'''
#多对多关系
class NewesType(models.Model):
    type_name = models.CharField(max_length=128)
    type_news = models.ManyToManyField('NewsInfo')

class NewsInfo(models.Model):

    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #关系属性
    news_type = models.ManyToManyField('NewesType')

class EmployeeBasicInfo(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    gebder = models.BooleanField(default=False)
    employDetail = models.OneToOneField('EmployDetailInfo')


class EmployDetailInfo(models.Model):
    addr = models.CharField(max_length=256)
    edu_exp = models.CharField(max_length=128)
    employBasic = models.OneToOneField('EmployeeBasicInfo')
'''

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)

    aParent = models.ForeignKey('self',null=True,blank=True)
