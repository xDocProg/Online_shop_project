from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema(tags=['Профиль'])
@extend_schema_view(
    get=extend_schema(
        summary='Получить профиль пользователя',
        description='Возвращает профиль текущего пользователя.',
    ),
    put=extend_schema(
        summary='Обновить профиль пользователя',
        description='Обновляет профиль текущего пользователя.',
        request=ProfileSerializer
    ),
    patch=extend_schema(
        summary='Частично обновить профиль пользователя',
        description='Частично обновляет профиль текущего пользователя.',
        request=ProfileSerializer
    )
)
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

