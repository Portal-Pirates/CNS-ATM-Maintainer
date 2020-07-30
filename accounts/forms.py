from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	#email = forms.EmailField(label= "Email")
	email = forms.EmailField(max_length=200, help_text='Required')
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']