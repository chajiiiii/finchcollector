from django.db import models

from django.urls import reverse

from datetime import date

MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner")
)

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=50)
    wingspan = models.CharField(max_length=50)
    colors = models.CharField(max_length=50)

    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse("detail", kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField("Feeding Date")
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    
    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-date"]