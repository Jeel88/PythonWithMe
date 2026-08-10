student = {
    "name": "Jeel",
    "age": 20,
    "course": "BTech IT",
    "college": "Engineering College"
}

print(student)
print(student["name"])
print(student.get("course"))
student["name"]="Jeel Savaliya"
print(student["name"])
student["city"] = "Mumbai"
print(student)
student.pop("college")
print(student)

print("name" in student)
print("email" in student)

print(len(student))

for key, value in student.items():
    print(key, value)