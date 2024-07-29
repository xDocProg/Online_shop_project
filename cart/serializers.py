from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор для элементов корзины пользователя """

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'total_price')


class CartSerializer(serializers.ModelSerializer):
    """ Сериализатор для корзины пользователя """

    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items', 'total_price']
