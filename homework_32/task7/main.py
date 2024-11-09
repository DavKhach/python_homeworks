import requests


url = "https://jsonplaceholder.typicode.com/invalid-url"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
