from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Категории'])
class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
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

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

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


class CategoryProductsListView(generics.GenericAPIView):
    """
    APIView для отображения списка продуктов по определенной категории
    """

    serializer_class = ProductSerializer

    @extend_schema(
        tags=['Категории'],
        summary='Получить продукты категории',
        description='Получаем список продуктов по id категории',
        request=ProductSerializer
    )
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'detail': 'Нет такой категории'}, status=404)

        products = Product.objects.filter(category=category).order_by('-id')
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
