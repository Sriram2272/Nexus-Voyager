import requests

url = "http://localhost:8000/run"
data = {
    "query": 'Execute action "generate_meal" with params: {"target_kcal":1000,"when":"day","diet":"vegetarian"}'
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:", response.json())
