from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    price_per_unit = models.FloatField()
    quantity = models.PositiveIntegerField()
