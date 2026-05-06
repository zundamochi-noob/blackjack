import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "gemma3:1b",
    "prompt": "hello",
    "stream": False
}

response = requests.post(url, json=data)
print(response.json()["response"])