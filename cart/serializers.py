from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор для элементов корзины пользователя """
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']


class CartSerializer(serializers.ModelSerializer):
    """ Сериализатор для корзины пользователя """

    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'cart_items', 'total_price']
