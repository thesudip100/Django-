from django.db import models
from datetime import datetime

# Create your models here
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
