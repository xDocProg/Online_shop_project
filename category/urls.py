from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView, CategoryProductsListView

app_name = 'category'

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='category_list_create'),
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('<int:category_id>/products/', CategoryProductsListView.as_view(), name='category-products-list'),
]