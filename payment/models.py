from decimal import Decimal

from django.db import models
from order.models import Order


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидается'),
        ('success', 'Успешный'),
        ('failed', 'Неудачный'),
        ('refunded', 'Возврат'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if self.order:
            self.amount = Decimal(self.order.total_price)
        super().save(*args, **kwargs)
        return self.amount

    def __str__(self):
        return f'Платеж {self.id} - {self.status}'
