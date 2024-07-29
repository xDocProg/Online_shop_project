from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView


urlpatterns = [
    path('', CartDetailView.as_view(), name='detail-cart'),
    path('add/', AddToCartView.as_view(), name='add-card'),
    path('remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-cart'),
]
