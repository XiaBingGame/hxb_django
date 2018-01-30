from django.conf.urls import url
from . import views
urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]{1,100})/$',
        views.post_detail,
        name='post_detail'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]{1,100})/$', views.post_test, name='post_test'),
    url(r'^archives/$', views.post_archive, name = 'post_archives'),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
]