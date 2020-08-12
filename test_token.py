import requests  # pip install requests

TOKEN = "7dcc37c6bb06a2f4880be7841d909ae6f8c116da"

headers = {
    "Authorization": f"Token {TOKEN}",
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())
