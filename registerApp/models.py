# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Register(models.Model) :		##table : registerApp_register
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email	= models.EmailField(max_length=254)
	mobilenumber	= models.CharField(max_length=14)
	dateofbirth = models.DateTimeField( null=True)
	gender = models.CharField(max_length=10)
	created_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s"%(format(self.email))

class Profile(models.Model) :			##table : registerApp_profile
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=150)
	signup_confirmation = models.BooleanField(default=False)

	def __str__(self) :
		return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs) :	
	if created :
		print "update_profile_signal in if created "
		Profile.objects.create(user=instance)### create data to registerApp_profile using user data from executing form.save() in views_usercreationform.py
	instance.profile.save()