squares = {}
for i in range(1, 6):
    squares[i] = i * i

print(squares)

# Dictionary comprehension
squares = {i: i * i for i in range(1, 6)}
print(squares)

# With condition
even_squares = {
    i: i * i
    for i in range(1, 11)
    if i % 2 == 0
}

print(even_squares)

# Using an existing list
numbers = [1, 2, 3, 4, 5]

square_dict = {number: number ** 2 for number in numbers}

print(square_dict)