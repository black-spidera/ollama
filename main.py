import requests

base_url = "http://localhost:11434/api/generate"  # Change back to localhost if running outside Docker

data = {
    "model": "tinyllama",
    "prompt": "Tell me about Shakila?",
    "stream": False
}

headers = {
    "Content-type": "application/json"
}

try:
    response = requests.post(base_url, json=data, headers=headers)
    if response.status_code==200:
        value = response.json()
        print(value["response"])
except Exception as e:
    print("Error occurred:", e)
