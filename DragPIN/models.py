from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Profile(models.Model):
    Identifiers =  (("A", "A"),("B", "B"),("C", "C"),("D", "D"),("E", "E"))
    DragID      = models.CharField(max_length=15, primary_key=True, unique=True)
    PIN         = models.CharField(max_length=4, validators=[RegexValidator(regex='[0-9][0-9][0-9][0-9]', message='Pin must be 4 numerics', code='invalid_Pin'),])
    fails       = models.PositiveSmallIntegerField(default=0)
    passes      = models.PositiveSmallIntegerField(default=0)
    #Identifier  = models.CharField(max_length=1, choices=Identifiers, default='A')
