from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Stud(models.Model):
    name = models.CharField('Name: ', max_length=20)
    surname = models.CharField('Surname: ', max_length=20)
    age = models.IntegerField('Age: ')
    gpa = models.FloatField('GPA: ')
    comment = models.TextField('Comment about university: ')

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('Group: ', max_length=20)
    sum_of_students = models.IntegerField('Sum of students: ')
    curator = models.CharField('Curator of the group: ', max_length=200)

    speciality = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField('Organization: ', max_length=100)
    type = models.CharField('Type of organization: ', max_length=100)
    sum_of_students = models.IntegerField('Sum of students: ')
    president = models.CharField('President of the group: ', max_length=200)

    def __str__(self):
        return self.name