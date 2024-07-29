from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework import permissions


class CartDetailView(generics.RetrieveAPIView):
    """ APIView для корзины пользователя """

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartView(generics.CreateAPIView):
    """ APIView для добавления товара в корзину """

    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class RemoveFromCartView(generics.DestroyAPIView):
    """ APIView для удаления товара из корзины """

    queryset = CartItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
