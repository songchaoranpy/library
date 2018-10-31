# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  django.db import models

#管理员
class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    uname = models.CharField(max_length=20)#管理员姓名
    psd = models.CharField(max_length=20)#管理员密码

    def __unicode__(self):
        return u'Reader:%s %s' %(self.uname,self.psd)
    class Meta:
        db_table = 't_user'

#读者表
class Reader(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    rname = models.CharField(max_length=20)#读者姓名
    tel = models.CharField(max_length=20)#读者电话
    def __unicode__(self):
        return u'User:%s%s'%(self.rname,self.tel)
    class Meta:
        db_table = 't_reader'
#图书类型表
class Type(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    type = models.CharField(max_length=20)#类型
    def __unicode__(self):
        return u'Type:%s'%(self.type)

    class Meta:
        db_table = 't_type'

#图书类
class Book(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    bookname = models.CharField(max_length=20,unique=True)#书名
    press = models.CharField(max_length=20)#出版社
    author = models.CharField(max_length=20)#作者
    type = models.ForeignKey(Type,on_delete=models.CASCADE)#分类
    count = models.IntegerField()#数量

    def __unicode__(self):
        return u'Book:%s%s%s%s%s'%(self.bookname,self.press,self.author,self.type,self.count)
    class Meta:
        db_table = 't_book'


#借书记录表
class Record(models.Model):

    id = models.AutoField(primary_key=True,unique=True)
    bookname = models.ForeignKey(Book,on_delete=models.CASCADE)#所借书名
    rname = models.ForeignKey(Reader,on_delete=models.CASCADE)#读者姓名
    borrow_data = models.DateField()#借书日期
    borrow_days = models.IntegerField()#借书时间
    def __unicode__(self):
        return u'Record:%s%s'%(self.borrow_data,self.borrow_days)
    class  Meta:
        db_table = 't_record'


