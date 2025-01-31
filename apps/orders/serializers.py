from rest_framework import serializers
from .models import Order, OrderItem
from apps.products.models import Product


# 1) Дополнительный вложенный сериализатор для чтения продукта
class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # Указываем только нужные поля
        fields = ['title', 'mainimg']


class OrderItemSerializer(serializers.ModelSerializer):

    # При создании/обновлении заказа передаем product_id
    product_id = serializers.PrimaryKeyRelatedField(
        source='product',           # Django будет подставлять в поле product
        queryset=Product.objects.all(),
        write_only=True
    )
    # При чтении заказа возвращаем подробную информацию о товаре
    product_info = ProductInfoSerializer(
        source='product',
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_info', 'quantity']


class CreateOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "delivery_address", "phone_number", "order_items"]

    def create(self, validated_data):
        """Создаёт заказ и связанные товары"""
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            # item_data['product'] будет содержать объект Product (из product_id)
            product = item_data["product"]
            quantity = item_data["quantity"]
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_order_time=product.price
            )

        order.save()  # Пересчёт общей суммы
        return order


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "user", "delivery_address", "phone_number",
            "amount", "order_items"
        ]
