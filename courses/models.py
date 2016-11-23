from django.db import models
from django.conf import settings

class Course(models.Model):
    name=models.CharField(max_length=255)
    short_description=models.CharField(max_length=255)     # краткое описание
    description=models.TextField(max_length=1255)      # полное описание
    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject=models.CharField(max_length=255)      # тема
    description=models.TextField(max_length=1255)         # описание
    course=models.ForeignKey(Course)   # курс
    order=models.PositiveIntegerField()        # номер по порядку
    def __str__(self):
        return self.subject



