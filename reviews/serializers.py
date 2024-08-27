from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор для отзывов """

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def validate(self, data):
        """ Проверка, что пользователь не оставлял отзыв на этот продукт """

        user = self.context['request'].user
        product = data.get('product')

        try:
            review = Review.objects.get(user=user, product=product)
            if self.instance and review.id == self.instance.id:
                # Если это обновление существующего отзыва, пропускаем проверку
                return data
        except Review.DoesNotExist:
            pass

        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("Вы уже оставляли отзыв на этот продукт.")

        return data

    def update(self, instance, validated_data):
        """ Обновление отзыва """
        instance.rating = validated_data.get('rating', instance.rating)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance




