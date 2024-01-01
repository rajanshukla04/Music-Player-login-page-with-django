from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name



