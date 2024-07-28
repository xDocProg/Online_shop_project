from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView


urlpatterns = [
    path('', CategoryAPIView.as_view(), name='category_list_create'),
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
]