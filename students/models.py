# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from courses.models import Course

# Create your models here.
class Student(models.Model):
	name = models.CharField(verbose_name = u'Имя', max_length=255, help_text='это имя')
	surname = models.CharField(verbose_name = u'Фамилия', max_length=255)
	date_of_birth = models.DateField(null = True, blank = True)
	email = models.EmailField(unique=True, null = True)
	phone = models.CharField(max_length=15, null = True, blank = True)
	address = models.CharField(max_length=100, null = True)
	skype = models.CharField(max_length=100, null = True,)
	courses = models.ManyToManyField(Course)

	def __str__(self):
		return self.surname