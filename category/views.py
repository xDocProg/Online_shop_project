from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Категории'])
class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAdminUser()]
        return [AllowAny()]

    @extend_schema(
        summary='Получить список категорий',
        description='Возвращает список всех категорий.',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        summary='Создать новую категорию',
        description='Создает новую категорию.',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema(tags=['Категории'])
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Получить категорию',
        description='Возвращает конкретную категорию по её ID.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Обновить категорию',
        description='Обновляет существующую категорию по её ID.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        summary='Частично обновить категорию',
        description='Частично обновляет существующую категорию по её ID.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Удалить категорию',
        description='Удаляет существующую категорию по её ID.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
