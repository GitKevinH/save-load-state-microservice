import requests

url = "http://127.0.0.1:5000/load"

body = {
    "username": "johnmayer",
    "application_name": "mayers_guitars"
}

response = requests.get(url, json=body)

if response.status_code == 200:
    message_returned = response.json()
    print(message_returned)
else:
    print(f"Something failed: {response.status_code}")