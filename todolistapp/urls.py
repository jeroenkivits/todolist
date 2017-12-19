from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^todo/$', views.todo_page, name='todo_page'),
    url(r'^weather/$', views.weather, name="weather"),
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^post_list/$', views.post_list, name='post_list'),
]
