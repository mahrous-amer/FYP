from django.db import models
from django import forms
from .models import LoginInfo
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

class SignUpForm(forms.ModelForm):
    user = forms.CharField(max_length=16)
    Question_one = forms.CharField(max_length=200)
    EmojiStr_one = forms.CharField(max_length=4, widget=EmojiPickerTextInputAdmin)
    Question_two = forms.CharField(max_length=200)
    EmojiStr_two = forms.CharField(max_length=4, widget=EmojiPickerTextInputAdmin)
    Question_three = forms.CharField(max_length=200)
    EmojiStr_three = forms.CharField(max_length=4, widget=EmojiPickerTextInputAdmin)

    class Meta:
        model = LoginInfo
        fields = ['user', 'Question_one', 'EmojiStr_one', 'Question_two', 'EmojiStr_two', 'Question_three', 'EmojiStr_three']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class LoginForm(forms.Form):
        username = forms.CharField(max_length=16)
        def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            ## add a "form-control" class to each form input
            ## for enabling bootstrap
            for name in self.fields.keys():
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
