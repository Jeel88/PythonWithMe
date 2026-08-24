import requests


base_url = "https://jsonplaceholder.typicode.com"


# GET

response = requests.get(f"{base_url}/posts/1")

print(response.status_code)
print(response.json())


# POST

data = {
    "title": "Python",
    "body": "Learning REST APIs",
    "userId": 1
}

response = requests.post(
    f"{base_url}/posts",
    json=data
)

print(response.status_code)
print(response.json())


# PUT

data = {
    "id": 1,
    "title": "Updated Python",
    "body": "Learning REST APIs",
    "userId": 1
}

response = requests.put(
    f"{base_url}/posts/1",
    json=data
)

print(response.status_code)
print(response.json())


# PATCH

data = {
    "title": "Python API"
}

response = requests.patch(
    f"{base_url}/posts/1",
    json=data
)

print(response.status_code)
print(response.json())


# DELETE

response = requests.delete(
    f"{base_url}/posts/1"
)

print(response.status_code)