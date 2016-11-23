from django.db import models
from django.conf import settings
from courses.models import Course

class Student(models.Model):
    name=models.CharField(max_length=255)         # имя
    surname=models.CharField(max_length=255)     # фамилия
    date_of_birth=models.DateField(null=True, blank=True)    # дата рождения 
    email=models.EmailField(unique=True, null=True)
    phone=models.CharField(max_length=15)    # телефон
    address=models.CharField(max_length=255)        # адрес
    skype=models.CharField(max_length=25)
    courses=models.ManyToManyField(Course, null=True, blank= True)   # курсы, на которых учится студент

    def __str__(self):
        return self.surname



