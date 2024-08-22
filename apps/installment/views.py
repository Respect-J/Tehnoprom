import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Installment
from .utils import calculate_annuity_payment
from apps.products.models import Product



class CalculateInstallmentView(APIView):
    def get(self, request, format=None):
        product_id = request.query_params.get('product_id')
        months = request.query_params.get('months', 6)

        if product_id is None or months is None:
            return Response({"error": "Product ID and months are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product_id = uuid.UUID(product_id)
            months = int(months)
        except ValueError:
            return Response({"error": "Invalid Product ID or months"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        total_amount = product.price

        installments = Installment.objects.all()
        response_data = []

        for installment in installments:
            monthly_payment = calculate_annuity_payment(total_amount, installment.percent, months)
            logo_url = request.build_absolute_uri(installment.logo.url)
            response_data.append({
                "title": installment.title,
                "logo": logo_url,
                "percent": installment.percent,
                "monthly_payment": monthly_payment
            })

        return Response(response_data, status=status.HTTP_200_OK)
