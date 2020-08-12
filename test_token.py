import requests  # pip install requests

# TOKEN = "7dcc37c6bb06a2f4880be7841d909ae6f8c116da"
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
    "eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNTk3MjA1ODg5LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTk3MjA1NTg5fQ."
    "aeB7uMDhy4M0yZC2Qrosu5zeQI81OuwvUM9DGUNCN1U"
)

# "eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNTk3MjAxNTYzLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTk3MjAxMjYzfQ" -- payload

headers = {
    "Authorization": f"JWT {JWT_TOKEN}",  # JWT 인증
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())

