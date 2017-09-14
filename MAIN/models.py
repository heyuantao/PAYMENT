# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class ItemModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50)