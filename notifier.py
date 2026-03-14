import os
import requests

BOT_TOKEN = "8693012928:AAHMXiuFdK4CuIBGEs_CZ4lcEPO2ZfxMfpk"
CHAT_ID = "1837766506"

def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=payload)