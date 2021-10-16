from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings


urlpatterns =[
    url(r'^todo/([0-9]+)$',views.TODOApi,name='todo'),
    url(r'^todo/$',views.TODOApi,name='todo'),
]