import os
import random

import barcode
from barcode.writer import ImageWriter
from django.conf import settings
from django.db import models

from cart.models import Cart
from users.models import CustomUser


class Order(models.Model):
    """ Модель заказа пользователя """

    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Отменено')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
    barcode = models.ImageField(upload_to='barcodes/', blank=True, null=True)

    def __str__(self):
        return f'Заказ {self.id} от {self.user.email or self.user.phone}'

    def generate_barcode(self):
        """Генерация штрих-кода для заказа."""

        barcode_data = ''.join(str(random.randint(0, 9)) for _ in range(12))
        ean = barcode.get('ean13', barcode_data, writer=ImageWriter())
        barcode_dir = os.path.join(settings.MEDIA_ROOT, 'barcodes')

        file_path = os.path.join(barcode_dir, f'{self.id}')
        ean.save(file_path)
        self.barcode = f'barcodes/{self.id}.png'



