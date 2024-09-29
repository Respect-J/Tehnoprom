from rest_framework import serializers
from .models import Product, PopularProduct
from decimal import Decimal, getcontext

def calculate_annuity_payment(P, monthly_rate, months):

    getcontext().prec = 28

    P = Decimal(P)
    r = Decimal(monthly_rate) / Decimal(100)
    n = Decimal(months)

    A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

    return int(A)


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.ReadOnlyField()
    instalments = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_instalments(self, obj):

        price = int(obj.price)
        monthly_rate = 5
        months = 12

        if price and price > 0:
            return calculate_annuity_payment(price, monthly_rate, months)
        return None




class PopularProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product', many=True)

    class Meta:
        model = PopularProduct
        fields = ['id', 'products']