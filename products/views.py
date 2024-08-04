from django.db.models import Avg
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


@extend_schema(tags=['Продукты'])
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.annotate(average_rating=Avg('reviews__rating'))
    serializer_class = ProductSerializer

    @extend_schema(
        summary='Получить список продуктов',
        description='Возвращает список всех продуктов.',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        summary='Создать новый продукт',
        description='Создает новый продукт.',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ----------------------------------------------------------------------------------


@extend_schema(tags=['Продукты'])
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.annotate(average_rating=Avg('reviews__rating'))
    serializer_class = ProductSerializer

    @extend_schema(
        summary='Получить продукт',
        description='Возвращает конкретный продукт по её ID.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Обновить продукт',
        description='Обновляет существующий продукт по её ID.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        summary='Частично обновить продукт',
        description='Частично обновляет существующий продукт по её ID.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Удалить продукт',
        description='Удаляет существующий продукт по её ID.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

