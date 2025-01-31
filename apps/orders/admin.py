from django.contrib import admin
from .models import Order, OrderItem



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'is_paid', 'amount')
    search_fields = ['id']         # поиск по 6-значному номеру
    list_filter = ['status', 'is_paid']  # фильтрация по статусу и оплате
    inlines = [OrderItemInline]    # прикрепляем inline для позиций заказа

