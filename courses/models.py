from django.db import models
from django.conf import settings
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)     
    description = models.TextField(max_length=1255)      
    coach = models.ForeignKey(Coach, related_name = 'coach_courses', null=True, blank= True)
    assistant = models.ForeignKey(Coach, related_name = 'assistant_courses', null=True, blank= True)
    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)      
    description = models.TextField(max_length=1255)        
    course = models.ForeignKey(Course)  
    order = models.PositiveIntegerField()        
    def __str__(self):
        return self.subject






