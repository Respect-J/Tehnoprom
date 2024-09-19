import os

import requests

token = os.getenv("TOKEN", "TOKEN")
headers = {
    'Authorization': f'Bearer {token}',
}


def send_verification_sms(phone_number, verification_code):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    payload = {
        "mobile_phone": phone_number,
        "message": f"Код подтверждения для регистрации на сайте texnoprom.net.uz: {verification_code}",
        "from": "4546",
        "callback_url": "http://0000.uz/test.php"

    }
    response = requests.post(url, data=payload, headers=headers)
    return response.status_code == 200
