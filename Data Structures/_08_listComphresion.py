numbers = []
for i in range(1, 6):
    numbers.append(i)
print(numbers)

squares = [i ** 2 for i in range(1, 6)]

# Numbers greater than 5
numbers = [1, 4, 7, 2, 9, 3]
large_numbers = [i for i in numbers if i > 5]

# Convert names to uppercase
names = ["jeel", "rahul", "aman"]
upper_names = [name.upper() for name in names]

print(squares)
print(large_numbers)
print(upper_names)