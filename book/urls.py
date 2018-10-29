#coding = utf-8
from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^$' ,views.bookmanage_view),
    url(r'login/' ,views.login_view),
    url(r'bookmanage/', views.manage_view),
    url(r'readmanage/', views.reader_view),

]