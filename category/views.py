from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Категории"],
    description="API для работы с категориями товаров."
)
class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
