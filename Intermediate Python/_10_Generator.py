# ==========================================
# Generators
# ==========================================


# ------------------------------------------
# 1. Basic Generator
# ------------------------------------------

def numbers():
    yield 1
    yield 2
    yield 3


for number in numbers():
    print(number)


# ------------------------------------------
# 2. Generator with next()
# ------------------------------------------

def values():
    yield 10
    yield 20
    yield 30


gen = values()

print(next(gen))
print(next(gen))
print(next(gen))


# ------------------------------------------
# 3. Generator with a Loop
# ------------------------------------------

def count_numbers(limit):

    for i in range(1, limit + 1):
        yield i


for number in count_numbers(5):
    print(number)


# ------------------------------------------
# 4. Even Number Generator
# ------------------------------------------

def even_numbers(limit):

    for number in range(limit + 1):

        if number % 2 == 0:
            yield number


for number in even_numbers(10):
    print(number)


# ------------------------------------------
# 5. Generator vs Return
# ------------------------------------------

def normal_function():
    return 10


def generator_function():
    yield 10
    yield 20
    yield 30


print(normal_function())

gen = generator_function()

print(next(gen))
print(next(gen))
print(next(gen))


# ------------------------------------------
# IMPORTANT
# ------------------------------------------

# return → gives value and ends the function
#
# yield → gives value and pauses the function
#
# Generator → produces values one at a time