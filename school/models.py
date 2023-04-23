from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, unique=True)
    
    def __str__(self):
        return self.name