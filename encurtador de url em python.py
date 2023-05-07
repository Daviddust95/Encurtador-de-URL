import requests
import json

access_token = "8e9d5422f15f9bcdd539d2e5db74f5cbec9780c0"
url = "https://api-ssl.bitly.com/v4/shorten"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "long_url": "https://www.google.com/"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_data = json.loads(response.text)
    short_url = response_data["link"]
    print(short_url)
else:
    print("Erro ao encurtar URL")
