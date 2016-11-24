from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=80)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Lessons(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return self.subject
    
