from django.db import models
from category.models import Category
from .validators.validators_price import validate_positive_price


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(validators=[validate_positive_price], max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name
