# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    uname = models.CharField(max_length=20)
    psd = models.CharField(max_length=20)

    def __unicode__(self):
        return u'Reader:%s %s' %(self.uname,self.psd)
    class Meta:
        db_table = 't_user'


class Reader(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    rname = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    def __unicode__(self):
        return u'User:%s%s'%(self.rname,self.tel)
    class Meta:
        db_table = 't_reader'

class Type(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    type = models.CharField(max_length=20)
    def __unicode__(self):
        return u'Type:%s'%(self.type)

    class Meta:
        db_table = 't_type'


class Book(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    bookname = models.CharField(max_length=20,unique=True)
    press = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    count = models.IntegerField()

    def __unicode__(self):
        return u'Book:%s%s%s%s%s'%(self.bookname,self.press,self.author,self.type,self.count)
    class Meta:
        db_table = 't_book'




class Record(models.Model):

    id = models.AutoField(primary_key=True,unique=True)
    bookname = models.ForeignKey(Book,on_delete=models.CASCADE)
    rname = models.ForeignKey(Reader,on_delete=models.CASCADE)
    borrow_data = models.DateField()
    borrow_days = models.IntegerField()
    def __unicode__(self):
        return u'Record:%s%s'%(self.borrow_data,self.borrow_days)
    class  Meta:
        db_table = 't_record'


