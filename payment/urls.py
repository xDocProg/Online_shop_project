from django.urls import path, include
from .views import PaymentDetailView, PaymentCreateView


urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='payment-create'),
    path('<int:order>/', PaymentDetailView.as_view(), name='payment-detail'),
]
