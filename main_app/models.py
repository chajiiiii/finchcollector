from django.db import models

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=50)
    wingspan = models.CharField(max_length=50)
    colors = models.CharField(max_length=50)