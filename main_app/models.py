from django.db import models

from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=50)
    wingspan = models.CharField(max_length=50)
    colors = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'finch_id': self.id})