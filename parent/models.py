from django.db import models
from django.contrib.auth.models import User
from school.models import *

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
    grade = models.IntegerField()
    section = models.CharField(max_length=1)
    choices = (
        ('At School', 'At School'),
        ('In Transit', 'In Transit'),
        ('Dismissed', 'Dismissed'),
    )
    status = models.CharField(max_length=20, choices=choices, default=choices[0][0])
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.parent.user.username