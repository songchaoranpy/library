#coding = utf-8
from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^info/' ,views.book_view),
    url(r'^login/' ,views.login_view),
]