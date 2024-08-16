from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView


app_name = 'products'

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='products_list_create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='products_detail'),
]
