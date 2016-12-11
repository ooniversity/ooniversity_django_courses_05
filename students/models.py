from django.db import models
from courses.models import Course

class Student(models.Model):
    """
    default docs
    """
    name = models.CharField(verbose_name='Student name', max_length=60)
    surname = models.CharField(verbose_name='Student surname', max_length=60)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=15, null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        return '%s %s' % (self.name, self.surname)
