from django.db import models
from django import forms
from .models import LoginInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000',]
Continent = [("1", "Africa"), ("2", "Asia"), ("3", "Antarctica"), ("4", "Europa"), ("5", "North America"), ("6", "South America"), ("7", "oceania/Australia")]
class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='choose your birth date',widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    question_text = forms.CharField(max_length=200)
    choice_text = forms.CharField(max_length=200, widget=EmojiPickerTextareaAdmin)
    bio = forms.CharField(max_length=500)
    location = forms.ChoiceField(choices=Continent)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'password', 'question_text', 'choice_text', 'birth_date', 'bio', 'location']
