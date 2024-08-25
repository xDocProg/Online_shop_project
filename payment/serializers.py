from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'status', 'payment_date']
        read_only_fields = ['amount', 'status']

    def validate(self, data):
        order = data.get('order')
        if Payment.objects.filter(order=order).exists():
            raise serializers.ValidationError("Платеж для этого заказа уже существует.")
        return data
