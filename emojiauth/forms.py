from django.db import models
from django import forms
from .models import LoginInfo
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

class SignUpForm(forms.ModelForm):
    user = forms.CharField(max_length=16)
    question_text = forms.CharField(max_length=200)
    choice_text = forms.CharField(max_length=200, widget=EmojiPickerTextInputAdmin)
    class Meta:
        model = LoginInfo
        fields = ['user', 'question_text', 'choice_text']

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
        Password_emoji = forms.CharField(max_length=16, widget=EmojiPickerTextInputAdmin)
        def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            ## add a "form-control" class to each form input
            ## for enabling bootstrap
            for name in self.fields.keys():
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
