from django.db import models
from django.conf import settings

class Coach(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()  # дата рождения
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ))
    phone = models.CharField(max_length=15)  # телефон
    address = models.CharField(max_length=255)  # адрес
    skype = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


    @property
    def get_name(self):
        return self.user.first_name

    def get_lastname(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email

    def get_staff(self):
        return self.user.staff_status

    def get_courses_coach(self):
        return self.coach_courses.filter(coach=self.id)

    def get_courses_assistent(self):
        return self.assistant_courses.filter(assistent=self.id)

    def __str__(self):
        return self.user.first_name