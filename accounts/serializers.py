from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    phone = serializers.CharField(source='user.phone', required=False)
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)

    class Meta:
        model = Profile
        fields = [
            'email', 'phone', 'first_name', 'last_name',
            'address', 'birth_date', 'profile_picture',
        ]

    def update(self, instance, validated_data):
        # Обновление данных CustomUser
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()

        # Обновление данных Profile
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
