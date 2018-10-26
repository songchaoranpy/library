#coding = utf-8
from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^$' ,views.login_view),
    url(r'^bookmanage' ,views.bookmanage_view),

]