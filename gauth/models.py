from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class LoginInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(help_text='Required. Format: YYYY-MM-DD',null=True)
    fails = models.PositiveSmallIntegerField(default=0)
    login_link = models.CharField(unique=True, blank=True, null=True, max_length=225)
    reset_link = models.CharField(unique=True, blank=True, null=True, max_length=225)
    question_text = models.CharField(null=True, max_length=200)
    choice_text = models.CharField(null=True, max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_LoginInfo(sender, instance, created, **kwargs):
    if created:
        LoginInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_LoginInfo(sender, instance, **kwargs):
    instance.LoginInfo.save()

@receiver(post_save, sender=User)
def update_user_LoginInfo(sender, instance, created, **kwargs):
    if created:
        LoginInfo.objects.create(user=instance)
    instance.LoginInfo.save()
