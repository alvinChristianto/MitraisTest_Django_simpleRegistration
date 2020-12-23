# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Register(models.Model) :
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email	= models.EmailField(max_length=254)
	mobilenumber	= models.CharField(max_length=14)
	dateofbirth = models.DateTimeField( null=True)
	gender = models.CharField(max_length=10)
	created_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s"%(format(self.email))