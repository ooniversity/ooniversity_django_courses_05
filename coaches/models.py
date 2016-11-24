from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings


class Coach(models.Model):
    user = models.OneToOneField(User,)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices = (('m', 'Male'), ('f', 'Female')))
    phone = models.CharField(max_length=15)    # телефон
    address = models.CharField(max_length=255)        # адрес
    skype = models.CharField(max_length=25)
    description = models.TextField()         
    
    def __str__(self):
        return self.user.first_name
    


