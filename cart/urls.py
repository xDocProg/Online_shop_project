from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView


app_name = 'cart'


urlpatterns = [
    path('', CartDetailView.as_view(), name='detail-cart'),
    path('add/', AddToCartView.as_view(), name='add-cart'),
    path('remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-cart'),
]
