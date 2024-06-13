import requests

from apps.orders.models import Order
from apps.products.serializers import ProductSerializer
from config.settings import TELEGRAM


def send_message(order: Order):
    bot_key: str = TELEGRAM.get("TOKEN")
    chat_id: int = TELEGRAM.get("CHAT_ID")

    products = []
    if order.products:
        products = ProductSerializer(order.products, many=True).data

    product_names = "\n".join([p["title"] for p in products])
    url: str = f"https://api.telegram.org/bot{bot_key}/sendMessage"
    message: str = f"""
    Заказ номер {order.id} оплачен.\n
    Номер телефона: {order.phone_number}.\n
    Адрес: {order.delivery_address}.\n
    Продукты: {product_names}
    """
    payload: dict = {"chat_id": chat_id, "text": message}
    response: requests.Response = requests.post(url=url, json=payload)

    response.raise_for_status()
