from django import forms
from django.forms import ModelForm
from .models import Register

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''
class NameForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)
'''

#MODELFORM
class NameForm(forms.ModelForm):		
	class Meta(object):
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



		CHOICES=(('M','Male'),('F','Female'))
		COLOR_CHOICES = (
		    ('green','GREEN'),
		    ('blue', 'BLUE'),
		    ('red','RED'),
		    ('orange','ORANGE'),
		    ('black','BLACK'),
		)
		#foo = forms.BooleanField(widget=widgets.RadioSelect(choices=[(1, 'Yes'), (2, 'No')]), initial='1')
		model = Register
		fields = ['firstname', 'lastname', 'email', 'mobilenumber', 'gender', 'dateofbirth']  #must be specified to Register fields
		widgets = {
			'mobilenumber' : forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Mobile Number +628',
					'value'	: '+6285729577104'
				}
			),
			'firstname' : forms.TextInput(		
				attrs={
					'class' : 'form-control',
					'placeholder' : 'first name',
					'value' : 'alvin'
				}
			),
			'lastname' : forms.TextInput(		
				attrs={
					'class' : 'form-control',
					'placeholder' : 'last name',
					'value' : 'alvin'
				}
			),
			'email' : forms.EmailInput(		
				attrs={
					'class' : 'form-control',
					'placeholder' : 'email address',
					'value' : 'alvin@dfd.com'
				}
			),
			'gender' : forms.RadioSelect(
				choices=CHOICES,
				attrs={
					'class' : 'custom-control-input'
				}
			)
		}

'''
class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=200)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', )

'''
class SignUpForm(UserCreationForm) :
	first_name = forms.CharField(max_length=30, help_text='First Name')
	last_name = forms.CharField(max_length=30, help_text='Last Name')
	email = forms.EmailField(max_length=200, help_text='Email')

	class Meta :
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

