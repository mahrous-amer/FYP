from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class LoginInfo(models.Model):
    user = models.CharField(max_length=15, primary_key=True, unique=True)
    fails = models.PositiveSmallIntegerField(default=0)
    login_link = models.CharField(unique=True, blank=True, null=True, max_length=225)
    reset_link = models.CharField(unique=True, blank=True, null=True, max_length=225)
    question_text = models.CharField(max_length=50)
    choice_text = models.CharField(max_length=20)

    def __str__(self):
        return self.user
