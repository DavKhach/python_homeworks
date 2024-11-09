import requests


url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(post["title"])
else:
    print(f"Failed to get posts: {response.status_code}")
