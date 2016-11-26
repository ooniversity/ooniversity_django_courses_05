from django.db import models
from django.conf import settings
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)     # краткое описание
    description = models.TextField(max_length=1255)      # полное описание
    coach = models.ForeignKey(Coach, related_name = 'coach_courses', null=True, blank= True)
    assistant = models.ForeignKey(Coach, related_name = 'assistant_courses', null=True, blank= True)
    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject=models.CharField(max_length=255)      # тема
    description=models.TextField(max_length=1255)         # описание
    course=models.ForeignKey(Course)   # курс
    order=models.PositiveIntegerField()        # номер по порядку
    def __str__(self):
        return self.subject






