from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from .models import Order
from .serializers import OrderSerializer


@extend_schema(tags=['Заказы'])
@extend_schema_view(
    get=extend_schema(
        summary='Получить заказы пользователя',
        description='Возвращает список заказов текущего пользователя.',
    ),
    post=extend_schema(
        summary='Создать новый заказ',
        description='Создает новый заказ для текущего пользователя.',
        request=OrderSerializer
    )
)
class OrderListCreateView(generics.ListCreateAPIView):
    """ APIView для создания заказа """

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        total_price = cart.total_price()
        serializer.save(user=self.request.user, cart=cart, total_price=total_price)


@extend_schema(tags=['Заказы'])
@extend_schema_view(
    get=extend_schema(
        summary='Получить заказ',
        description='Возвращает конкретный заказ текущего пользователя.'
    ),
    put=extend_schema(
        summary='Обновить заказ',
        description='Обновляет конкретный заказ текущего пользователя.',
        request=OrderSerializer
    ),
    patch=extend_schema(
        summary='Частично обновить заказ',
        description='Частично обновляет конкретный заказ текущего пользователя.',
        request=OrderSerializer
    ),
    delete=extend_schema(
        summary='Удалить заказ',
        description='Удаляет конкретный заказ текущего пользователя.'
    )
)
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

