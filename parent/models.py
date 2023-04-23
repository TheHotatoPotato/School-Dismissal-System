from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    section = models.CharField(max_length=1)

    def __str__(self):
        return self.name + ' - ' + self.parent.user.username