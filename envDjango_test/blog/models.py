from django.db import models
import time

#设计和表对应的类，模型类

# Create your models here.


class BookInfo(models.Model):
    '''图书模型类'''
    #CharField说明是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)

    #说明是一个日期类型
    bpub_date = models.DateField()


    def __str__(self):
        return self.btitle

#关系属性 hbook,建立图书类和英雄人物类之间的一对多关系
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=False)

    hcomment = models.CharField(max_length=128)

    hbook = models.ForeignKey("BookInfo",on_delete=models.CASCADE)