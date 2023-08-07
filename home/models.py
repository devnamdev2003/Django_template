from django.db import models
from django.contrib import messages

# Create your models here.


class ContactInfo(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    number = models.CharField(max_length=15)
    mess = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
