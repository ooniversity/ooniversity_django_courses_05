from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
	user=models.OneToOneField(User) #пользоваетль
	date_of_birth=models.DateField() #дата рождения
	gender=models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
	phone=models.CharField(max_length=13)
	address=models.CharField(max_length=150)
	skype=models.CharField(max_length=150)
	description=models.TextField()
	def __str__(self):
		return self.user.username

	@property
	def full_name(self):
		return "{0} {1}".format(self.user.first_name, self.user.last_name)

# Create your models here.
