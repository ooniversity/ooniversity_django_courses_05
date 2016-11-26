from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)  # имя
    surname = models.CharField(max_length=100)  # фамилия
    date_of_birth = models.DateField()  # дата рождения
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # телефон
    address = models.CharField(max_length=255)  # адрес
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
