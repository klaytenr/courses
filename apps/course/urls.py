from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'courses$', views.index),
    url(r'courses/create$', views.create),
    url(r'courses/delete/(?P<id>\d+)$', views.confirm),
    url(r'courses/destroy/(?P<id>\d+)$', views.delete),
]
