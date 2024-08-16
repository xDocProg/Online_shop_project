from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView


app_name = 'category'

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='category_list_create'),
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
]