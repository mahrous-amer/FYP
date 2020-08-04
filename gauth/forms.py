from django import forms
from .models import LoginInfo
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Format: YYYY-MM-DD')
    question_text = forms.CharField(max_length=200)
    choice_text = forms.CharField(max_length=200)
    bio = forms.CharField(max_length=500)
    location = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username','bio','email','location','birth_date','question_text','choice_text' )
