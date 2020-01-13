from django.db import models

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