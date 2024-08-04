from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework import permissions
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    get=extend_schema(
        summary='Получить корзину пользователя',
        description='Возвращает корзину текущего пользователя.',
        tags=['Корзина']
    )
)
class CartDetailView(generics.RetrieveAPIView):
    """ APIView для корзины пользователя """

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

# -------------------------------------------------------------------------


@extend_schema_view(
    post=extend_schema(
        summary='Добавить товар в корзину',
        description='Добавляет товар в корзину текущего пользователя.',
        tags=['Корзина']
    )
)
class AddToCartView(generics.CreateAPIView):
    """ APIView для добавления товара в корзину """

    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


# -------------------------------------------------------------------------

@extend_schema_view(
    delete=extend_schema(
        summary='Удалить товар из корзины',
        description='Удаляет товар из корзины текущего пользователя.',
        tags=['Корзина']
    )
)
class RemoveFromCartView(generics.DestroyAPIView):
    """ APIView для удаления товара из корзины """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
