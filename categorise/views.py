from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
import os

# Create your views here.

from django.http import HttpResponse


class Home_page(TemplateView):

    template_name = 'index.html'