from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import ReviewSerializer
from .models import Review
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@extend_schema(tags=['Отзывы'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список отзывов',
        description='Возвращает список всех отзывов.',
    ),
    create=extend_schema(
        summary='Создать новый отзыв',
        description='Создает новый отзыв для продукта. Требует аутентификации.',
    ),
    retrieve=extend_schema(
        summary='Получить отзыв',
        description='Возвращает конкретный отзыв по его ID.',
    ),
    partial_update=extend_schema(
        summary='Частичное обновление отзыва',
        description='Позволяет частично обновить отзыв. Можно обновить только некоторые поля.',
    ),
    update=extend_schema(
        summary='Обновить отзыв',
        description='Обновляет существующий отзыв по его ID. Требует аутентификации.',
    ),
    destroy=extend_schema(
        summary='Удалить отзыв',
        description='Удаляет существующий отзыв по его ID. Требует аутентификации.',
    ),
)
class ReviewViewSet(viewsets.ModelViewSet):
    """ APIView для отзывов """

    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

