from drf_spectacular.utils import extend_schema_view, extend_schema
from .serializers import ReviewSerializer
from .models import Review
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@extend_schema_view(
    list=extend_schema(
        summary='Получить список отзывов',
        description='Возвращает список всех отзывов.',
        tags=['Отзывы']
    ),
    create=extend_schema(
        summary='Создать новый отзыв',
        description='Создает новый отзыв для продукта. Требует аутентификации.',
        tags=['Отзывы']
    ),
    retrieve=extend_schema(
        summary='Получить отзыв',
        description='Возвращает конкретный отзыв по его ID.',
        tags=['Отзывы']
    ),
    partial_update=extend_schema(
        summary='Частичное обновление отзыва',
        description='Позволяет частично обновить отзыв. Можно обновить только некоторые поля.',
        tags=['Отзывы']
    ),
    update=extend_schema(
        summary='Обновить отзыв',
        description='Обновляет существующий отзыв по его ID. Требует аутентификации.',
        tags=['Отзывы']
    ),
    destroy=extend_schema(
        summary='Удалить отзыв',
        description='Удаляет существующий отзыв по его ID. Требует аутентификации.',
        tags=['Отзывы']
    ),
)
class ReviewViewSet(viewsets.ModelViewSet):
    """ APIView для отзывов """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

