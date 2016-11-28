# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null = True)
    date_of_birth = models.DateField(null = True, blank = True)
    instructor = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=instructor, default='m')
    phone = models.CharField(max_length=15, null = True, blank = True)
    address = models.CharField(max_length=100, null = True)
    skype = models.CharField(max_length=100, null = True)
    description = models.TextField(null = True,)

    #def __str__(self):
     #   return self.username

#user1:Gaitavr1 pass:qwerty12345 name:Mozes mail:gaitavr@example.com
#user2:Kolombo pass:zxcvbnm12345 name:piter mail:piter_falk@hotmail.com
#user2:Ventura pass:asdfghjkl12345 name:Ace mail:ace_ventura@gmail.com