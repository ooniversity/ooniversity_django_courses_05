from django.db import models
from django.conf import settings
from courses.models import Course

class Student(models.Model):
    name=models.CharField(max_length=60)         # имя
    surname=models.CharField(max_length=60)     # фамилия
    date_of_birth=models.DateField()    # дата рождения 
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)    # телефон
    address=models.CharField(max_length=255)        # адрес
    skype=models.CharField(max_length=25)
    courses=models.ManyToManyField(Course)   # курсы, на которых учится студент

    def full_name(self):
        self.full_n = self.name + " " + self.surname
        return self.full_n
    def __str__(self):
        return self.full_name()
    




