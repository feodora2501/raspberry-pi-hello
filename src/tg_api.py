import httpx

from config import TOKEN

token = TOKEN
base_url=f"https://api.telegram.org/bot{token}"

client = httpx.Client()

def get_chat_id():
    raw_response = client.get(
        url=f"{base_url}/getUpdates"
        )

    response = raw_response.json()
    chat_id = response["result"][0]["message"]["chat"]["id"]
    
    return chat_id


def send_message(ip):
    chat_id = get_chat_id()

    response = client.post(
        url=f"{base_url}/sendMessage",
        params={
            "chat_id": chat_id,
            "text": ip
        }
    )
    
    return response
