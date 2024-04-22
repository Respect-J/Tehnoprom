from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .api import NasiyaAPI
from .models import CalculateTariff, CheckStatus, ConfirmContract, CreateOrder


class CheckStatusView(APIView):
    def post(self, request, *args, **kwargs):
        status = CheckStatus(**request.data)
        nasiya_api = NasiyaAPI()
        return Response(nasiya_api.check_status(status))


class CalculateTariffsView(APIView):
    def post(self, request, *args, **kwargs):
        tariff = CalculateTariff(**request.data)
        nasiya_api = NasiyaAPI()
        return Response(nasiya_api.calculate_tariffs(tariff))


class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        order = CreateOrder(**request.data)
        nasiya_api = NasiyaAPI()
        return Response(nasiya_api.create_order(order))


class ConfirmContractView(APIView):
    def post(self, request, *args, **kwargs):
        contract = ConfirmContract(**request.data)
        nasiya_api = NasiyaAPI()
        return Response(nasiya_api.confirm_contract(contract))
