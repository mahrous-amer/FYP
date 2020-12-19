# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save
import random, emoji
from .randemoji import random_emoji
# Create your models here.

class LoginInfo(models.Model):
    user             = models.CharField(max_length=15, primary_key=True, unique=True)
    fails            = models.PositiveSmallIntegerField(default=0)
    login_link       = models.CharField(unique=True, blank=True, null=True, max_length=225)
    reset_link       = models.CharField(unique=True, blank=True, null=True, max_length=225)

    #   Question 1
    Question_one     = models.CharField(max_length=50)
    EmojiStr_one     = models.TextField(max_length=100)
    EmojiArray_one   = models.CharField(max_length=100)
    PIN_one          = models.CharField(max_length=4)
    #   Question 2
    Question_two     = models.CharField(max_length=50)
    EmojiStr_two     = models.TextField(max_length=100)
    EmojiArray_two   = models.CharField(max_length=100)
    PIN_two          = models.CharField(max_length=4)


    def __str__(self):
        return self.user

    def start(self):
        for x in range(2):
            if x == 0:
                emojisraw = str(emoji.demojize(self.EmojiStr_one)).split(':')
                emojisraw = list(filter(None, emojisraw))
                pinarr = []
                for x in emojisraw:
                    pinarr.append(emoji.emojize(f":{x}:"))
                Question = self.Question_one
                #pinarr = list(self.EmojiStr_one)
                EmojiArray = [random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6)]
                for i in pinarr:
                    EmojiArray.append(i)
                    random.shuffle(EmojiArray)
                print(EmojiArray)
                self.EmojiArray_one = EmojiArray
                for i in pinarr:
                    print(i)
                    x = EmojiArray.index(i)
                    self.PIN_one += str(x)
                print(self.PIN_one)
            if x == 1:
                emojisraw = str(emoji.demojize(self.EmojiStr_two)).split(':')
                emojisraw = list(filter(None, emojisraw))
                pinarr = []
                for x in emojisraw:
                    pinarr.append(emoji.emojize(f":{x}:"))
                Question = self.Question_two
                EmojiArray = [random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6), random_emoji(6)]
                for i in pinarr:
                    print(i)
                    EmojiArray.append(i)
                    random.shuffle(EmojiArray)
                print(EmojiArray)
                self.EmojiArray_two = EmojiArray
                for i in pinarr:
                    x = EmojiArray.index(i)
                    self.PIN_two += str(x)
                print(self.PIN_two)


    def GetEmojiArray(self):
        options = [1, 2]
        random.shuffle(options)
        if options[0] == 1:
            return self.Question_one, self.PIN_one, self.EmojiArray_one, options[0]
        if options[0] == 2:
            return self.Question_two, self.PIN_two, self.EmojiArray_two, options[0]

    def GetAnEmojiArray(self, Question):
        if Question == 1:
            return self.Question_one, self.PIN_one, self.EmojiArray_one
        if Question == 2:
            return self.Question_two, self.PIN_two, self.EmojiArray_two
