from django.shortcuts import render
from django.views.generic import TemplateView


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home_page.as_view(), name='home')
]
