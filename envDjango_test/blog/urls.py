from django.urls import path
from blog import views
from django.conf.urls import url

urlpatterns = [
    #通过url函数设置url函数配置
    # url(r'^',views.index),#建立views和url之间的关系
    path('index',views.index),
    url(r'^favoriteBook',views.favoriteBook),
    url(r'^books$',views.show_books),
    url(r'^books/(\d+)$', views.detail),#显示英雄信息

]

