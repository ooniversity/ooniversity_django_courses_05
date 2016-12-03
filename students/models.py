from django.db import models
from courses.models import Course


class Student(models.Model):

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_courses(self):
        return Course.objects.filter(student=self)

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)