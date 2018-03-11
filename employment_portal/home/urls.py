from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home', views.IndexView.as_view(), name='index'),
]