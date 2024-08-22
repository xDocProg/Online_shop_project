from rest_framework import serializers

from cart.serializers import CartItemSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания заказа """

    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'updated_at', 'total_price', 'order_items', 'barcode']
        read_only_fields = ['user', 'total_price', 'created_at', 'updated_at', 'barcode']

    def create(self, validated_data):
        # Создание нового заказа
        order = Order.objects.create(**validated_data)
        # Генерация штрих-кода
        order.generate_barcode()
        order.save()
        return order









