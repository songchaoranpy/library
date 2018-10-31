#coding = utf-8
from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^$' ,views.bookmanage),
    url(r'^index/' ,views.index),
    url(r'login/' ,views.login),
    url(r'bookmanage/', views.manage),
    url(r'readmanage/', views.reader),
    url(r'addbook/', views.addbook),
    url(r'booktype/', views.booktype),
    url(r'addtype/', views.addtype),
    url(r'addread/', views.addread),
    url(r'^bookBorrow/', views.bookBorrow),
    url(r'^bookRenew/', views.bookRenew),
    url(r'^bookBack/', views.bookBack),

]