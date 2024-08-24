from django.db import models
from products.models import Product
from reviews.validators import validate_profanity
from users.models import CustomUser


class Review(models.Model):
    """ Модель отзывов """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
    comment = models.TextField(validators=[validate_profanity], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.user} к {self.product.name}'

