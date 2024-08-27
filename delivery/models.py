from django.conf import settings
from django.db import models
from order.models import Order


class Delivery(models.Model):
    """
    Модель адреса доставки
    """

    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('in_transit', 'В пути'),
        ('delivered', 'Доставлено'),
        ('failed', 'Неудача')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery_order')
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Сохраняем доставку
        super().save(*args, **kwargs)

        # Обновляем статус заказа, если статус доставки изменился на 'delivered'
        if self.status == 'delivered':
            order = self.order
            if order.status != 'delivered':
                order.status = 'delivered'
                order.save()

    def __str__(self):
        return f'Доставка для заказа {self.order.id}'
