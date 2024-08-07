import requests

url = "your_ngrok_url/predict"
data = {"text": "The market is performing well today."}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
