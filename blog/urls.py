from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),
]