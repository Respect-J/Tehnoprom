from dataclasses import asdict, dataclass

import requests

from config.settings import UZUM

from . import models


@dataclass
class NasiyaAPI:
    def _api_call(self, route: str, payload: dict | None = None) -> dict:
        if payload is None:
            return {}
        token: str = UZUM.get("UZUM_TOKEN")
        base_url: str = UZUM.get("UZUM_BASE_URL")

        headers: dict = {"Authorization": f"Bearer {token}"}
        full_url: str = f"{base_url}{route}"
        response: requests.Response = requests.post(url=full_url, headers=headers, json=payload)
        return {
            "status": response.status_code,
            "message": response.json(),
        }

    def check_status(self, info: models.CheckStatus) -> dict:
        route: str = "/api/v3/uzum/buyer/check-status"
        return self._api_call(route, asdict(info))

    def calculate_tariffs(self, info: models.CalculateTariff) -> dict:
        """
        @user_id: Uzum Nasiya User ID
        product: Product at partner end
        {
            "user_id": 108,
            "products": [
                {
                    "price": 10000,
                    "amount": 1,
                    "product_id": 1
                }
            ]
        }

        Only verified users can calculate tariffs (use check_status endpoint first)
        """
        route: str = "/api/v3/mfo/calculate"
        return self._api_call(route, asdict(info))

    def create_order(self, info: models.CreateOrder) -> dict:
        """
        'create_order' could possibly be renamed to 'create_contract'
        """
        route: str = "/api/v3/mfo/order"
        return self._api_call(route, asdict(info))

    def confirm_contract(self, info: models.ConfirmContract) -> dict:
        route: str = "/api/v3/uzum/contract-confirm"
        return self._api_call(route, asdict(info))
