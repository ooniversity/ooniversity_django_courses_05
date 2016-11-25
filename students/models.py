import datetime
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=90, verbose_name='Student name') #имя
    surname = models.CharField(max_length=90, verbose_name='Student surname') #фамилия
    date_of_birth = models.DateField() #дата рождения
    email = models.EmailField(unique=True) #почта
    phone = models.CharField(max_length=13, null=True, blank=True) #телефон
    address = models.CharField(max_length=255) #адрес
    skype = models.CharField(max_length=40, null=True, blank=True) 
    courses = models.ManyToManyField(Course) #курсы на которы хучится студент
    def __str__(self):
        return self.name

# Create your models here.
