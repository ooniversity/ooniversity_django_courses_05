from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from students.models import Student
from django import forms
from django.contrib import messages


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype','courses']



