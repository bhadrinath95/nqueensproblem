'''
Created on 04-Jul-2020

@author: BHADRINATH
'''
from django.urls import path, re_path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.home, name='display'),
]