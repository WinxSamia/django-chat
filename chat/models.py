from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=1000000)
class Messages(models.Model):
    user=models.CharField(max_length=1000000)
    name=models.CharField(max_length=100000)
    value=models.CharField(max_length=1000000)
    date=models.DateTimeField(default=datetime.now, blank = True)
