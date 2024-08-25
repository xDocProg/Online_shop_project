from rest_framework import serializers

from delivery.models import Delivery
from payment.models import Payment
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
        fields = [
            'id', 'user', 'status', 'created_at', 'updated_at', 'total_price', 'order_items',
            'barcode_image', 'barcode_number'
        ]
        read_only_fields = ['user', 'total_price', 'created_at', 'updated_at', 'barcode_image', 'barcode_number']

    def create(self, validated_data):
        # Создание нового заказа
        order = Order.objects.create(**validated_data)
        # Генерация штрих-кода
        order.generate_barcode()
        order.save()
        return order

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)

        # Проверяем, если статус меняется на 'received'
        if new_status == 'received':
            # Проверяем, есть ли успешная оплата для этого заказа
            if not Payment.objects.filter(order=instance, status='success').exists():
                raise serializers.ValidationError("Вы не можете получить товар, пока не оплатите заказ")

            delivery = Delivery.objects.filter(order=instance).first()
            if not delivery or delivery.status != 'delivered':
                raise serializers.ValidationError("Вы не можете получить заказ так как ваш товар не доставлен")

        # Обновляем статус и другие поля
        instance.status = new_status
        instance.save()
        return instance








