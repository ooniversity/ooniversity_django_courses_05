# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Course(models.Model):
	name = models.CharField(verbose_name = u'Название курса', max_length=255, help_text='This is name')
	short_description = models.CharField(verbose_name = u'краткое описание', max_length=255) 
	description = models.TextField(verbose_name = u'полное описание')

	def __str__(self):
		return self.name

class Lesson(models.Model):
	subject = models.CharField(verbose_name = u'Тема', max_length=255, help_text='This is name')
	description = models.TextField(verbose_name = u'описание')
	course = models.ForeignKey(Course)
	order = models.PositiveIntegerField()
	
	def __str__(self):
		return self.subject