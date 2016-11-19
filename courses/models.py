from django.db import models


class Course(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=50)
    description = models.TextField()


class Lesson(models.Model):
    def __str__(self):
        return self.subject

    subject = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()