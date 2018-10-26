# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import User


def book_view(request):

    return render(request, 'book.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        luname = request.POST.get('luname','')
        lpwd = request.POST.get('lpwd','')
        count = User.objects.filter(uname=luname ,psd=lpwd).count()
        if count == 1:
            return render(request,'book.html')
        else:
            return HttpResponse('321')


