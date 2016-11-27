from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    skype = models.CharField(max_length=64)
    description = models.TextField()
    
    def __str__(self):
        return self.user.username
    


