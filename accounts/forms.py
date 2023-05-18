from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phone', 'image']


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
