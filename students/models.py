from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def full_name(self):
        return '%s %s' % (self.name, self.surname)

    def __str__(self):
        return self.full_name()

    def get_courses(self):
        return Course.objects.filter(student=self)