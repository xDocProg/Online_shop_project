from rest_framework import viewsets, permissions
from order.models import Order
from .models import Delivery
from .serializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().order_by('-updated_at')
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order_id = self.request.data.get('order')
        order = Order.objects.get(id=order_id)
        if order.user != self.request.user:
            raise permissions.PermissionDenied("Вы не можете сделать доставку для этого заказа.")
        serializer.save(user=self.request.user)

