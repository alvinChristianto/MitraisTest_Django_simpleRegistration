# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request) :
	context = {
		'title' : 	'register ',
		'page' 	:	'register page', 
	}
	return render(request, 'register.html', context)	

def recent(request) :
	return render(request, 'recent.html')
