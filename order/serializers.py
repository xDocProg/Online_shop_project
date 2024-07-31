from rest_framework import serializers

from cart.serializers import CartItemSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(source='cart.items', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'total_price', 'cart_items']
        read_only_fields = ['total_price', 'created_at']
