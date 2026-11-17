import requests

url = "http://127.0.0.1:5000/save"

body = {
    "username": "johnmayer",
    "application_name": "mayers_guitars",
    "data": {
        "brand": "PRS",
        "model": "Silver_Sky",
        "color": "red"
    }

}

response = requests.post(url, json=body)

if response.status_code == 201:
    message_returned = response.json()
    print(message_returned['filename'], message_returned['status'] )
else:
    print(f"Something failed: {response.status_code}")