from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=254)
    scientific_name = models.CharField(max_length=254)
    owner_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    contact = models.CharField(max_length=12)
    address = models.TextField()
