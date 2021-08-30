from django.db import models

# Create your models here.

class fruit(models.Model):
    genus = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    id = models.IntegerField(primary_key=True)
    family = models.CharField(max_length=150)
    order = models.CharField(max_length=150)
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calories = models.FloatField()
    sugar = models.FloatField()
    image = models.CharField(max_length=556)
