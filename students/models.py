import datetime
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=90, verbose_name='Student name')
    surname = models.CharField(max_length=90, verbose_name='Student surname')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=40, null=True, blank=True) 
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name

    
    def full_name(self):
        return '%s %s' % (self.name, self.surname)