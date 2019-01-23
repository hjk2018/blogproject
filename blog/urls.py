from django.conf.urls import url

from . import views

'''
我们的网址是用正则表达式写的，Django 会用这个正则表达式去匹配用户实际输入的网址，
如果匹配成功，就会调用其后面的视图函数做相应的处理
Django 首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，此时只剩下一个空字符串，
而 r'^$' 的模式正是匹配一个空字符串（这个正则表达式的意思是以空字符串开头且以空字符串结尾），
于是二者匹配，Django 便会调用其对应的 views.index 函数。
'''

# 以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，如 post/1/、 post/255/ 等都是符合规则的，[0-9]+ 表示一位或者多位数
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # archives 视图函数的实际调用为：archives(request, year=2017, month=3)
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
