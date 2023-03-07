# -*- coding: utf-8 -*-
# @Time    : 2023/3/7 18:28
# @Author  : AI悦创
# @FileName: forms.py.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
