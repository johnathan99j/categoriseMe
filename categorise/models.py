# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sentence(models.Model):
    text = models.CharField(max_length=300)
    isPositive = models.BooleanField(default=True)
    percetange = models.IntegerField(default=0)

