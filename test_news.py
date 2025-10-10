import requests, json

r = requests.post("http://127.0.0.1:8000/run", json={"query":"Give me top 3 technology news"})
print("Status:", r.status_code)
print("Response:", r.json())
