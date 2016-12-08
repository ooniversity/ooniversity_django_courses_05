from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=90)
    short_description = models.CharField(max_length=255)
    description = models.TextField(default=None)
    coach=models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant=models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=90)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def __str__(self):
        return self.subject
    def __repr__(self):
        return self.subject
