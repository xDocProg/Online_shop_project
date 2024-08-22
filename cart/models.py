from decimal import Decimal

from django.db import models
from products.models import Product
from users.models import CustomUser


class Cart(models.Model):
    """ Модель для корзины пользователя """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя: {self.user}'

    def total_price(self):
        return sum(item.price() for item in self.cart_items.all())


class CartItem(models.Model):
    """ Модель для элементов корзины пользователя """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} {self.product.name}'

    def price(self):
        return self.quantity * self.product.price




