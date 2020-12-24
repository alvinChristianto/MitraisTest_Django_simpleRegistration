# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import ContactForm

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Register
from registerApp.serializers import RegisterSerializer
from rest_framework.decorators import api_view


def index(request) :
	return render(request, 'index_registerApp.html')	


def newuser(request) :
	contextError = {}
	contextSuccess = {}
	success_data = {}


	def chkName(strText) :
		if strText.isalpha() == False :
			error = "name is invalid"
			return (0,error)
		else :
			return (1,strText)

	def chkMobilenumber(mobNumber):
		if mobNumber[:4] != "+628" :
			error = "Mobile Number invalid, should use +62"
			return (0,error)
		else :
			return (1,mobNumber)


	if request.method == 'POST':	
		check_firstname	= chkName(request.POST['firstname'])
		check_lastname	= chkName(request.POST['lastname'])
		check_mobilenumber	= chkMobilenumber(request.POST['mobilenumber'])
	
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


		print "contextError error %s" %(contextError)
		print "success %s" %(success_data)
	
		if len(contextError) == 0 :
			data = Register(
					firstname=success_data['firstname'], 
					lastname=success_data['lastname'], 
					email=request.POST['email'], 
					mobilenumber=request.POST['mobilenumber'], 
					dateofbirth="2020-12-22 00:00:00.000000", 
					gender="M" )
			data.save()
			contextSuccess = {
				'message' : "data successfully insert !"
			}


	return render(request, 'register.html', {'error'	: contextError,
											 'success'	: contextSuccess})

def listuser(request) :
	item = Register.objects.all()
	context = {
		'item' 	:	item,
	}
	return render(request, 'listuser.html', context)


def loginuser(request, pk) :
	try:
		RegisterData = Register.objects.get(email=pk)
	except ObjectDoesNotExist:
		print("Either the blog or entry doesn't exist.")

##--------------##
'''
@api_view(['GET', 'POST', 'DELETE'])
def register_user(request):
	if request.method == 'GET':
		register = Register.objects.all()
        
		id_register = request.GET.get('id', None)
		if id_register is not None:
			register = register.filter(id__contains=id_register)
        
		register_serializer = RegisterSerializer(register, many=True)
		return JsonResponse(register_serializer.data, safe=False)
        # 'safe=False' for objects serialization

	elif request.method == 'POST':
		register_data = JSONParser().parse(request)
		register_serializer = RegisterSerializer(data=register_data)
		if register_serializer.is_valid():
			register_serializer.save()
			return JsonResponse(register_serializer.data, status=status.HTTP_201_CREATED) 
		return JsonResponse(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
	elif request.method == 'DELETE':
		count = Register.objects.all().delete()
		return JsonResponse({'message': '{} user deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def register_detail(request, pk):
	try: 
		register = Register.objects.get(pk=pk) 
	except Register.DoesNotExist: 
		return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
	if request.method == 'GET': 
		register_serializer = RegisterSerializer(register) 
		return JsonResponse(register_serializer.data) 
 

	elif request.method == 'PUT': 
		register_data = JSONParser().parse(request) 
		register_serializer = RegisterSerializer(register, data=register_data) 
		if register_serializer.is_valid(): 
			register_serializer.save() 
			return JsonResponse(register_serializer.data) 
		return JsonResponse(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
	elif request.method == 'DELETE': 
		register.delete() 
		return JsonResponse({'message': 'user deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def register_list(request):
	register = Register.objects.filter(published=True)
        
	if request.method == 'GET': 
		register_serializer = RegisterSerializer(register, many=True)
		return JsonResponse(register_serializer.data, safe=False)
'''