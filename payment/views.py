from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response

from .serializers import PaymentSerializer
from .models import Payment
from rest_framework import generics, status


@extend_schema(tags=['Платежи'])
@extend_schema_view(
    post=extend_schema(
        summary='Обрабатывает платеж',
        description='Возвращает статус платежа. По умолчанию success'
    )
)
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status='success')
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@extend_schema(tags=['Платежи'])
@extend_schema_view(
    get=extend_schema(
        summary='Получить описание платежа',
        description='Возвращает описание платежа по id заказа'
    )
)
class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'order'




