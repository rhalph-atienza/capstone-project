# Django forms are defined here. Forms are used when allowing a user to input data when creating a new or updating a database entry.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Use a valid email address.')
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('is_artist', 'bio', 'commissions_open', 'commission_rates', 'genre')

