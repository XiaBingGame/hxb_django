from django.conf.urls import url
from django.contrib import admin
from hxb_blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]
