from django.db import models

from cart.models import Cart
from users.models import CustomUser


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Отменено')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)

    def __str__(self):
        return f'Заказ {self.id} от {self.user.email or self.user.phone}'



