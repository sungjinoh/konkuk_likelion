# -*- coding: utf-8 -*-
from django.db import models
class Apply(models.Model):
	user = models.CharField(max_length=32)
	phone = models.CharField(max_length=32)
	colleage = models.CharField(max_length=32)
	email = models.CharField(max_length=32)
	introduction = models.CharField(max_length=1024)
	service = models.CharField(max_length=1024)
