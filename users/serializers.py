from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers
from .models import CustomUser, ConfirmationCode
from .tasks import send_confirmation_email


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ Создаем сериализатор для регистрации пользователя """

    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if not data.get('email') and not data.get('phone'):
            raise serializers.ValidationError('Введите номер телефона или email')
        return data

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data.get('email'),
            phone=validated_data.get('phone', None)
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        code = ConfirmationCode.generate_code()
        expires_at = timezone.now() + timezone.timedelta(minutes=2)
        ConfirmationCode.objects.create(user=user, code=code, expires_at=expires_at)

        # Вызов задачи кода подтверждения на email
        send_confirmation_email.delay(user.email, code)
        return user


class ConfirmEmailSerializer(serializers.Serializer):
    """ Создаем сериализатор для подтверждения кода электронной почты """

    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)


class LoginSerializer(serializers.Serializer):
    """ Создаем сериализатор для входа в систему """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)

        if user and user.is_active:
            return {'user': user}
        raise serializers.ValidationError('Неправильно введенные данные')


