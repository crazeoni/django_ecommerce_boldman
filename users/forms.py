from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
	email=forms.EmailField(max_length=64, help_text='Enter a valid email address')
	attrs={'class': 'form-control', 'placeholder': 'Email'}
	class Meta:
		model = User
		fields = ['username', 'email']
		labels = {}
