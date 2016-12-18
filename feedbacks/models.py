# -*- coding: utf-8 -*-
from django.db import models
#from datetime import datetime

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(verbose_name=u'имя отправителя', max_length=55)
    subject = models.CharField(verbose_name=u'тема сообщения', max_length=255)
    message = models.TextField(verbose_name=u'сообщение')
    from_email = models.EmailField(unique=True, null = True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_email

