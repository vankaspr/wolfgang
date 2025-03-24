from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True,  blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username

