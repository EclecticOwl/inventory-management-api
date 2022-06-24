from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    price_per_unit = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
