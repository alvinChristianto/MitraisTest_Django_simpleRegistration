# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from forms import ContactForm

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Register
from registerApp.serializers import RegisterSerializer
from rest_framework.decorators import api_view

from .forms import NameForm
#----
import calendar
import re
from datetime import datetime


def django_form(request) :
	contextError = {}
	contextSuccess = {}
	contextDMY = {}


	success_data = {}

	now = datetime.now()
	print now
	year = now.strftime("%Y")

	def DictDMY() :
		contextDay = []
		contextMonth = []
		contextYear = []

		for day_idx in range(1,32) :
			contextDay.append(day_idx)

		for month_idx in range(1, 13):
			#contextMonth[calendar.month_name[month_idx]] = calendar.month_name[month_idx]
			contextMonth.append(calendar.month_name[month_idx])

		for year_idx in range(80):
			#contextMonth[calendar.month_name[month_idx]] = calendar.month_name[month_idx]
			contextYear.append(int(year) - year_idx)

		contextDMY['day'] = contextDay
		contextDMY['month'] = contextMonth
		contextDMY['year'] = contextYear

	def chkName(strText) :
		if strText.isalpha() == False :
			error = "name is invalid"
			return (0,error)
		else :
			return (1,strText)

	def chkMobilenumber(mobNumber):
		'''
		if mobNumber[:4] != "+628" :
			error = "Mobile Number invalid, should use +62"
			return (0,error)
		else :
			return (1,mobNumber)
		'''
		if len(mobNumber) < 12 or len(mobNumber) > 15 :
			error = "please check length of mobile number"
			return (0, error) 
		else :
			x = re.match("^\+628", mobNumber)
			if x:
				if mobNumber[4:].isdigit() == True :
					return (1, mobNumber)
				else :
					error = "Mobile Number cannot contain letter and special character"
					return (0, error)
			else:			
				error = "Mobile number must contain +628"
				return (0, error)

	DictDMY()

	if request.method == 'POST' :
		form = NameForm(request.POST)
		#if form.is_valid() :		#need to use something like usercreationform from modelform django
		check_firstname	= chkName(request.POST['firstname'])
		check_lastname	= chkName(request.POST['lastname'])
		check_mobilenumber	= chkMobilenumber(request.POST['mobilenumber'])
		check_DOB = "%s-%s-%s"%(request.POST['selectYear'], list(calendar.month_name).index(request.POST['selectMonth']), request.POST['selectDate'])
		
		if check_firstname[0] == 1 :
			success_data["firstname"] = check_firstname[1]
		elif check_firstname[0] == 0 :
			contextError["error_firstname"]= check_firstname[1]


		if check_lastname[0] == 1 :
			success_data["lastname"] = check_lastname[1]
		elif check_lastname[0] == 0 :
			contextError["error_lastname"]= check_lastname[1]

		if check_mobilenumber[0] == 1 :
			success_data["mobilenumber"] = check_mobilenumber[1]
		elif check_mobilenumber[0] == 0 :
			contextError["error_mobilenumber"]= check_mobilenumber[1]

		if Register.objects.filter(email=request.POST['email']):	#filter return 1 or more, get return only 1
			contextError["error_email"]= "Email already registered"
		else : 
			print "~~~~~~email good to go"


		print "contextError error %s" %(contextError)
		print "success %s" %(success_data)
	
		if len(contextError) == 0 :
			data = Register(
					firstname=success_data['firstname'], 
					lastname=success_data['lastname'], 
					email=request.POST['email'], 
					mobilenumber=success_data["mobilenumber"], 
					dateofbirth=check_DOB, 
					gender=request.POST['gender'] )
			#data.save()
			contextSuccess = {
				'message' : "data successfully insert !"
			}

	else :
		form = NameForm()

	return render(request, 'register_djangoform.html', {'form'			: form,
														'error'			: contextError,
											 			'success'		: contextSuccess,
														'DayMonthYear' 	: contextDMY})
