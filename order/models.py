import os
import random

import barcode
from barcode.writer import ImageWriter
from django.conf import settings
from django.db import models
from users.models import CustomUser


class Order(models.Model):
    """
    Модель заказа пользователя
    """

    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Отменено'),
        ('received', 'Получено')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
    barcode_image = models.ImageField(upload_to='barcodes/', blank=True, null=True)
    barcode_number = models.CharField(max_length=13, unique=True, blank=True, null=True)

    def __str__(self):
        return f'Заказ {self.id} от {self.user.email}'

    def generate_barcode(self):
        """
        Генерация уникального номера штрих-кода и изображения штрих-кода для заказа.
        """

        barcode_data = ''.join(str(random.randint(0, 9)) for _ in range(12))
        ean = barcode.get('ean13', barcode_data, writer=ImageWriter())
        barcode_dir = os.path.join(settings.MEDIA_ROOT, 'barcodes')
        file_path = os.path.join(barcode_dir, f'{self.id}')
        ean.save(file_path)

        self.barcode_image = f'barcodes/{self.id}.png'
        self.barcode_number = ean


class OrderItem(models.Model):
    """
    Модель для элементов заказа
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product} в заказе {self.order.id}'


