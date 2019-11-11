import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Pet(models.Model):
    petName=models.CharField(max_length=200)
    petBorn_time=models.DateTimeField('date born')

class Petdata(models.Model):
    IdtoPet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    data1=models.IntegerField(default=0)
    data2=models.FloatField(default=0)

class Tp(models.Model):
    data1=models.FloatField(default=0)
    data2=models.FloatField(default=0)