import json

student = {
    "name": "Jeel",
    "age": 20,
    "skills": ["Python", "Java", "React"]
}

json_data = json.dumps(student)

print(json_data)



# import json

# data = '{"name": "Jeel", "age": 20}'

# student = json.loads(data)

# print(student)
# print(student["name"])