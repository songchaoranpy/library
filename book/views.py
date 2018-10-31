# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import *

#首页
def bookmanage(request):

    books = Book.objects.all()
    return render(request, 'bookmanage.html', {'books': books})

#登录
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        uname = request.POST.get('name','')
        upwd = request.POST.get('pwd','')
        cont = User.objects.filter(name=uname,psd=upwd).count()
        if  cont:
            return render(request,'bookmanage.html')
        else:
            return HttpResponse('<script>alert("用户名或密码有误");location.href="/index/"</script>')


#更改管理员
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        luname = request.GET.get('luname', '')
        lpwd = request.GET.get('lpwd', '')
        count = User.objects.filter(uname=luname, psd=lpwd).count()
        if count == 1:
            return render(request, 'bookmanage.html')
        else:
            return render(request,'login.html')

#图书管理
def manage(request):
    books = Book.objects.all()
    return render(request, 'manage.html', {'books': books})


#添加图书
def addbook(request):
    if request.method == "GET":
        return render(request,'addbook.html')
    else:
        bname = request.POST.get('bookname','')
        bpress = request.POST.get('press','')
        bauthor = request.POST.get('author','')
        btype = request.POST.get('booktype','')
        bcount = request.POST.get('bookcount','')
        if bname and bpress and bauthor and btype and bcount:
            books = Book(bookname=bname,press=bpress,author=bauthor,type_id=btype,count=bcount)
            books.save()
            return render(request,'successful.html')
        else:
            return render(request,'failure.html')

#图书类型展示
def booktype(request):
    types = Type.objects.all()
    return render(request,'booktype.html',{'types':types})

#添加图书类型
def addtype(request):
    if request.method == 'GET':
        return render(request, 'addtype.html')
    else:
        tname = request.POST.get('typename','')
        if tname:
            type = Type(type=tname)
            type.save()
            return render(request,'successful.html')
        else:
            return render(request,'failure.html')

# 读者管理
def reader(request):
    reads = Reader.objects.all()
    return render(request, 'read.html', {'reads': reads})



#添加读者
def addread(request):
    if request.method == 'GET':
        reads = Reader.objects.all()
        return render(request, 'addread.html', {'reads': reads})
    else:
        rname = request.POST.get('rname','')
        rtel = request.POST.get('rtel','')
        if rname and rtel:
            read = Reader(rname=rname,tel=rtel)
            read.save()
            return render(request,'successful.html')
        else:
            return render(request, 'failure.html')

#借阅
def bookBorrow(request):
    if request.method == 'GET':
        return render(request,'bookBorrow.html')
    else:
        return HttpResponse('123')

#续借
def bookRenew(request):
    return render(request,'bookRenew.html')

#归还
def bookBack(request):
    return render(request,'bookBack.html')