from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, permissions
from order.models import Order
from .models import Delivery
from .serializers import DeliverySerializer


@extend_schema(tags=['Доставка'])
@extend_schema_view(
    list=extend_schema(
        summary='Список доставок',
        description='Возвращает список всех доступных доставок. Требуется аутентификация.',
    ),
    retrieve=extend_schema(
        summary='Получить детали доставки',
        description='Возвращает информацию о конкретной доставке по её ID. Требуется аутентификация.',
    ),
    create=extend_schema(
        summary='Создать новую доставку',
        description='Создает новую доставку для заказа. Пользователь может создать доставку только для своих заказов. '
                    'Требуется аутентификация.',
    ),
    update=extend_schema(
        summary='Обновить доставку',
        description='Обновляет существующую доставку. Требуется аутентификация.',
    ),
    partial_update=extend_schema(
        summary='Частичное обновление доставки',
        description='Частично обновляет данные существующей доставки. Требуется аутентификация.',
    ),
    destroy=extend_schema(
        summary='Удалить доставку',
        description='Удаляет существующую доставку по её ID. Требуется аутентификация.',
    ),
)
class DeliveryViewSet(viewsets.ModelViewSet):
    """
    APIView для доставки
    """

    queryset = Delivery.objects.all().order_by('-updated_at')
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order_id = self.request.data.get('order')
        order = Order.objects.get(id=order_id)
        if order.user != self.request.user:
            raise permissions.PermissionDenied("Вы не можете сделать доставку для этого заказа.")
        serializer.save(user=self.request.user)

