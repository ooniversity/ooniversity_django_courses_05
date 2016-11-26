from django.db import models
from django.utils import timezone
import datetime
from django.utils.encoding import python_2_unicode_compatible

class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    course  = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField('date_of_birth')
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)	
    courses = models.ManyToManyField(Course)
