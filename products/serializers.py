from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'average_rating']

    def validate(self, data):
        if data.get('price') <= 0:
            raise serializers.ValidationError('Price не может быть меньше или равен 0')
        return data


