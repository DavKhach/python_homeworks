import requests


url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My Title",
    "body": "This is the body of the post",
    "userId": 26
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Post created:", response.json())
else:
    print(f"Failed to create post: {response.status_code}")
