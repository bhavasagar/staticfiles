from django.db import models

# Create your models here.
class UserRegistrationForm(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)