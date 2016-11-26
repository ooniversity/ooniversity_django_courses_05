from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(verbose_name=u'имя', max_length=200)
    surname = models.CharField(verbose_name=u'фамилия', max_length=200)
    date_of_birth = models.DateField(verbose_name=u'дата рождения')
    email = models.EmailField()
    phone = models.CharField(verbose_name=u'телефон', max_length=200)
    address = models.CharField(verbose_name=u'адрес', max_length=200)
    skype = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)


    def __str__(self):
        return self.name

