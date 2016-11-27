from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length= 1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length= 10)
    address = models.CharField(max_length= 100)
    skype = models.CharField(max_length= 100)
    description = models.TextField()


    def get_first_name(self):
        return self.user.first_name

    def get_last_name(self):
        return self.user.last_name

    def full_name(self):
        return self.get_first_name() + ' ' + self.get_last_name()

    def get_user_email(self):
        return self.user.email

    def __str__(self):
        return self.user.first_name


