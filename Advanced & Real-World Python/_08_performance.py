import time


# List lookup

numbers = list(range(1000000))

start = time.time()

print(999999 in numbers)

end = time.time()

print("List time:", end - start)


# Set lookup

numbers = set(range(1000000))

start = time.time()

print(999999 in numbers)

end = time.time()

print("Set time:", end - start)


# Slow approach

start = time.time()

result = []

for number in range(1000000):
    if number % 2 == 0:
        result.append(number)

end = time.time()

print("Loop time:", end - start)


# Better approach

start = time.time()

result = [number for number in range(1000000) if number % 2 == 0]

end = time.time()

print("Comprehension time:", end - start)


# Generator

def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number


numbers = even_numbers(1000000)

print(next(numbers))
print(next(numbers))
print(next(numbers))


# Avoid unnecessary repeated work

numbers = [1, 2, 3, 4, 5]

# Slow

start = time.time()

for _ in range(100000):
    total = sum(numbers)

end = time.time()

print("Repeated calculation:", end - start)


# Better

start = time.time()

total = sum(numbers)

for _ in range(100000):
    result = total

end = time.time()

print("Stored result:", end - start)