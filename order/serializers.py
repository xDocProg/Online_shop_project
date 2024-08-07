from django.conf import settings
from rest_framework import serializers

from cart.serializers import CartItemSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания заказа """

    cart_items = CartItemSerializer(source='cart.items', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'total_price', 'cart_items', 'barcode']
        read_only_fields = ['total_price', 'created_at', 'barcode']

    def create(self, validated_data):
        # Создание нового заказа
        order = Order.objects.create(**validated_data)
        # Генерация штрих-кода
        order.generate_barcode()
        order.save()
        return order






