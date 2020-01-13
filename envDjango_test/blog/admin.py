from django.contrib import admin
from blog.models import BookInfo
#后台管理相关的文件
# Register your models here.

#自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

#注册模型类
admin.site.register(BookInfo,BookInfoAdmin)
