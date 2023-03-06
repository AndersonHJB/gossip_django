# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 22:42
# @Author  : AI悦创
# @FileName: urls.py.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
