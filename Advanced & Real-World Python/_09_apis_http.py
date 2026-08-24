import requests


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)


for user in data:
    print(user["name"], user["email"])


url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    user = response.json()

    print(user["name"])
    print(user["email"])
else:
    print("Request failed")


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python",
    "body": "Learning APIs",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())