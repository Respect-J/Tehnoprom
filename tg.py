import requests

from config.settings import TELEGRAM


def send_message(order_id: str):
    bot_key: str = TELEGRAM.get("TOKEN")
    chat_id: int = TELEGRAM.get("CHAT_ID")

    url: str = f"https://api.telegram.org/bot{bot_key}/sendMessage"
    message: str = f"Заказ номер {order_id} оплачен"
    payload: dict = {"chat_id": chat_id, "text": message}
    response: requests.Response = requests.post(url=url, json=payload)

    response.raise_for_status()
