from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
from .randemoji import random_emoji
# Create your models here.

class LoginInfo(models.Model):
    user             = models.CharField(max_length=15, primary_key=True, unique=True)
    fails            = models.PositiveSmallIntegerField(default=0)
    login_link       = models.CharField(unique=True, blank=True, null=True, max_length=225)
    reset_link       = models.CharField(unique=True, blank=True, null=True, max_length=225)

#   Question 1
    Question_one     = models.CharField(max_length=50)
    EmojiStr_one     = models.CharField(max_length=20)
    EmojiArray_one   = models.CharField(max_length=20)
    PIN_one          = models.CharField(max_length=4)
    #   Question 2
    Question_two     = models.CharField(max_length=50)
    EmojiStr_two     = models.CharField(max_length=20)
    EmojiArray_two   = models.CharField(max_length=20)
    PIN_two          = models.CharField(max_length=4)
    #   Question 3
    Question_three   = models.CharField(max_length=50)
    EmojiStr_three   = models.CharField(max_length=20)
    EmojiArray_three = models.CharField(max_length=20)
    PIN_three        = models.CharField(max_length=4)

    def __str__(self):
        return self.user

    def start(self):
        for x in range(3):
            if x == 0:
                Question = self.Question_one
                pinarr = list(self.EmojiStr_one)
                EmojiArray = [random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6)]
                for i in pinarr:
                    EmojiArray.append(i)
                    random.shuffle(EmojiArray)
                    print(EmojiArray)
                self.EmojiArray_one = ' '.join([str(elem) for elem in EmojiArray])
                for i in pinarr:
                    x = EmojiArray.index(i)
                    self.PIN_one += str(x)
            if x == 1:
                Question = self.Question_two
                pinarr = list(self.EmojiStr_two)
                EmojiArray = [random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6)]
                for i in pinarr:
                    EmojiArray.append(i)
                    random.shuffle(EmojiArray)
                    print(EmojiArray)
                self.EmojiArray_two = ' '.join([str(elem) for elem in EmojiArray])
                for i in pinarr:
                    x = EmojiArray.index(i)
                    self.PIN_two += str(x)
            if x == 2:
                Question = self.Question_three
                pinarr = list(self.EmojiStr_three)
                EmojiArray = [random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6)]
                for i in pinarr:
                    EmojiArray.append(i)
                    random.shuffle(EmojiArray)
                    print(EmojiArray)
                self.EmojiArray_three = ' '.join([str(elem) for elem in EmojiArray])
                for i in pinarr:
                    x = EmojiArray.index(i)
                    self.PIN_three += str(x)

    def GetEmojiArray(self):
        options = [1, 2, 3]
        random.shuffle(options)
        if options[0] == 1:
            return self.Question_one, self.PIN_one, self.EmojiArray_one
        if options[0] == 2:
            return self.Question_two, self.PIN_two, self.EmojiArray_two
        if options[0] == 3:
            return self.Question_three, self.PIN_three, self.EmojiArray_three
