from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='post_new'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='post_edit'),
    url(r'^todo/$', views.todo_page, name='todo_page'),
    url(r'^weather/$', views.weather, name="weather"),
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^post_list/$', views.todo_page, name='todo_list'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
