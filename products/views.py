from django.db.models import Avg
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.annotate(average_rating=Avg('reviews__rating'))
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.annotate(average_rating=Avg('reviews__rating'))
    serializer_class = ProductSerializer
