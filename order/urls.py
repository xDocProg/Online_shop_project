from django.urls import path
from .views import OrderListCreateView, OrderDetailView


app_name = 'order'


urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
