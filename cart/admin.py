from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price')
    list_filter = ('created_at',)
    search_fields = ('user__email',)

    def total_price(self, obj):
        return obj.total_price()


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')
    list_filter = ('cart__user', 'product')
    search_fields = ('cart__user__email', 'product__name')

    def total_price(self, obj):
        return obj.total_price()


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
