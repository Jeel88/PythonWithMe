import os


name = os.getenv("USER_NAME")

print(name)


api_key = os.getenv("API_KEY")

if api_key:
    print("API key found")
else:
    print("API key not found")


database_password = os.getenv("DB_PASSWORD")

print(database_password)