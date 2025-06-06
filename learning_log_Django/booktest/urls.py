
from django.conf.urls import include, url
from booktest import views


urlpatterns = [
   url(r'^index$',views.index,name='index'),
   url(r'^show_index2$', views.show_index2),
   url(r'^create$',views.create),
   url(r'^delete(\d+)$',views.delete),
   url(r'^error$',views.error),
   url(r'^shownum(\d+)$', views.show_num),#捕获url参数,位置参数
   url(r'^shownamenum(?P<num>\d+)$', views.show_namenum),#捕获url参数,位置参数
   url(r'^login$',views.login),#显示登陆页面
   url(r'^login_check$',views.login_check),
   url(r'^test_ajax$', views.ajax_test),
   url(r'^ajax_handle$',views.ajax_handle),
   url(r'^set_cookie$',views.set_cookie),
   url(r'get_cookie$',views.get_cookie),
   url(r'^set_session$',views.set_session),
   url(r'^get_session$', views.get_session),
   url(r'^clear_session$',views.clear_session),
   url(r'^temp_var$',views.temp_var),
   url(r'^temp_inherit$',views.temp_inherit),
   url(r'^html_escape$',views.html_escape),
   url(r'^url_reverse$',views.url_reverse),
   url(r'^change_pwd$',views.change_pwd),
   url(r'^change_pwd_action$',views.change_pwd_action),
   url(r'^show_area(?P<pindex>\d*)$',views.show_area),
   url(r'^areas$',views.areas),
   url(r'^prov$',views.prov),
   url(r'^city(\d+)$',views.city),
   url(r'^return_json$',views.return_json),
   url(r'^interface_login$',views.interface_login),


]
