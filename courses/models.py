from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=90) #имя курса
    short_description = models.CharField(max_length=255) #краткое описание
    description = models.TextField(null=True, blank=True) #полное описание
    def __str__(self):
        return self.name #возвращает название курса

class Lesson(models.Model):
    subject = models.CharField(max_length=90, verbose_name="Theme") #тема урока
    description = models.TextField() #описание темы курса
    course = models.ForeignKey(Course) #сам курс
    order = models.PositiveIntegerField(verbose_name="Lesson number")
    def __str__(self):
        return self.subject # возвращает тему урока
    def __repr__(self):
        return self.subject
# Create your models here.
