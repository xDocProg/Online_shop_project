from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import ConfirmationCode, CustomUser
from .serializers import UserRegistrationSerializer, ConfirmEmailSerializer, LoginSerializer
from drf_spectacular.utils import extend_schema


class RegisterViewSet(generics.CreateAPIView):
    """ APIView для регистрации пользователя """

    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['Регистрация'],
        summary="Регистрация нового пользователя",
        description='Создает нового пользователя и отправляет код подтверждения на email',
        request=UserRegistrationSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'detail': 'Код подтверждения отправлен на ваш email'
            },
            status=status.HTTP_201_CREATED
        )


class ConfirmEmailView(generics.GenericAPIView):
    """ APIView для подтверждения кода для email """

    serializer_class = ConfirmEmailSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Подтверждение email',
        description='Подтверждает email пользователя по отправленному коду',
        request=ConfirmEmailSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        try:
            user = CustomUser.objects.get(email=email)
            confirmation_code = ConfirmationCode.objects.get(user=user, code=code)

            if confirmation_code.has_expired():
                return Response(
                    {
                        'error': 'Срок действия кода подтверждения истек'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.is_email_verified = True
            user.is_active = True
            user.save()
            confirmation_code.delete()

            return Response(
                {
                    'detail': 'Email подтвержден, и пользователь активирован'
                },
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        except ConfirmationCode.DoesNotExist:
            return Response({'detail': 'Код подтверждения не найден'}, status=status.HTTP_404_NOT_FOUND)


class LoginView(generics.GenericAPIView):
    """ APIView для входа в систему """

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['Вход'],
        summary='Вход в систему',
        description='Аутентифицирует пользователя и возвразщает JWT токены',
        request=LoginSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = RefreshToken.for_user(user)

        return Response(
            {
                'refresh': str(token),
                'access': str(token.access_token)
            },
            status=status.HTTP_200_OK
        )







