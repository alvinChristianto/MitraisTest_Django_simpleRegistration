from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.template.loader import render_to_string

from django.core.mail import EmailMessage

from .forms import SignUpForm
from .tokens import account_activation_token

'''
def signup_view(request) :
	form = UserCreationForm(request.POST)
	if form.is_valid() :
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('home')

	return render(request, 'register_usercreationform.html', {'form': form})

'''
def activation_sent_view(request) :
	return render(request, 'activation_sent.html')

def activate(request, uidb64, token) :
	try :
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token) :
		user.is_active = True
		user.profile.signup_confirmation = True
		user.save()
		login(request, user)
		return redirect('/')
	else :
		return render(request, 'activation_invalid.html')

def signup_view(request) :
	if request.method == 'POST' :
		form = SignUpForm(data=request.POST)
		print "creating form %s"%(form.is_valid())
		if form.is_valid() :
			print "enter if"
			user = form.save()
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
			user.is_active = False
			user.save()			#will trigger signal decorator in models.py (post_save)
			current_site = get_current_site(request)
			subject = 'Please activate your account'
			message = render_to_string('activation_request.html', {
				'user' : user,
				'domain' : current_site.domain,
				'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
				'token' : account_activation_token.make_token(user),
			})
			#user.email_user(subject, message) #testing only not sent via smtp
			email = EmailMessage(
				subject, message, to=[user.profile.email]
			)
			email.send()

			#username = form.cleaned_data.get('username')
			#password = form.cleaned_data.get('password1')
			#user = authenticate(username=username, password=password)
			#login(request, user)
			print "~~~~~seharusnya sukse"
			return redirect('activation_sent')
	else :
		form = SignUpForm()
	return render(request, 'register_usercreationform.html', {'form': form})
'''

def signup_view(request):
	form = SignUpForm(data=request.POST)
	print form.is_valid()
	if form.is_valid():
		print "its valid"
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/listuser/')
	else:
		form = SignUpForm()
	return render(request, 'register_usercreationform.html', {'form': form})
'''