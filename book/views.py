# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import *

#首页
def bookmanage_view(request):

    books = Book.objects.all()
    return render(request, 'bookmanage.html', {'books': books})

# 登录
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        luname = request.GET.get('luname', '')
        lpwd = request.GET.get('lpwd', '')
        count = User.objects.filter(uname=luname, psd=lpwd).count()
        if count == 1:
            return render(request, 'bookmanage.html')
        else:
            return HttpResponse('321')

#图书管理
def manage_view(request):
    books = Book.objects.all()
    return render(request, 'manage.html', {'books': books})


def reader_view(request):
    reads = Reader.objects.all()

    return render(request,'read.html',{'reads':reads})