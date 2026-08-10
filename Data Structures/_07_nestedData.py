numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers)

print(numbers[0])
print(numbers[0][0])
print(numbers[1][2])

students = [
    {
        "name": "Jeel",
        "age": 20
    },
    {
        "name": "Rahul",
        "age": 21
    },
    {
        "name": "Aman",
        "age": 19
    }
]
print(students)
print(students[0]["name"])
print(students[1]["name"])
for i in students:
    print(i["name"] , i["age"])
students[0]["location"]="Mumbai"
print(students)    