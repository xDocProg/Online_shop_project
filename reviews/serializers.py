from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор для отзывов """

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']


