
from django.conf.urls import include, url
from InterfaceAutoTest import views


urlpatterns = [
   url(r'^index$',views.index,name='index'),
   url(r'^login$',views.login),


]
