import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc0MzY1MjIsImlhdCI6MTcyNDg0NDUyMiwicm9sZSI6InRl" \
        "c3QiLCJzaWduIjoiODRmMWU3NjJkZTRhMWU4N2JlODJkZmYxMTUwNGQ2ZmZkNjc4ZmRhZTAxNTY4MjhkNzU2OWU0YWYyMmYyZTg3NCIsI" \
        "nN1YiI6IjgyNzkifQ.Ql8Xlx04kJKN_EOak9qM29fXCFDPkaqhXyq3t8fRtEE"
headers = {
    'Authorization': f'Bearer {token}',
}


def send_verification_sms(phone_number, verification_code):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    payload = {
        "mobile_phone": phone_number,
        "message": verification_code,
        "from": "4546",
        "callback_url": ""

    }
    response = requests.post(url, data=payload, headers=headers)
    return response.status_code == 200
