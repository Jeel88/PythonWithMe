# ==========================================
# Mutability & Immutability
# ==========================================


# ------------------------------------------
# 1. Mutable Object - List
# ------------------------------------------

numbers = [1, 2, 3]

print("Before:", numbers)

numbers.append(4)

print("After:", numbers)


# ------------------------------------------
# 2. Same List Reference
# ------------------------------------------

a = [1, 2, 3]

b = a

b.append(4)

print("a:", a)
print("b:", b)

# Both changed because a and b
# refer to the same list.


# ------------------------------------------
# 3. Immutable Object - Integer
# ------------------------------------------

x = 10

print("Before:", x)

x = 20

print("After:", x)

# The integer 10 itself was NOT changed.
# x was simply made to refer to another object.


# ------------------------------------------
# 4. Immutable Object - String
# ------------------------------------------

name = "Jeel"

# This does NOT modify the existing string.
# It creates a new string.

name = name + " Savaliya"

print(name)


# ------------------------------------------
# 5. Trying to Modify a String
# ------------------------------------------

name = "Jeel"

# This would cause an error:
#
# name[0] = "X"
#
# Strings are immutable.


# ------------------------------------------
# 6. Mutable Dictionary
# ------------------------------------------

student = {
    "name": "Jeel",
    "age": 20
}

student["age"] = 21

print(student)

# Dictionary can be changed,
# so it is mutable.


# ------------------------------------------
# 7. Mutable Set
# ------------------------------------------

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)

# Sets are mutable.


# ------------------------------------------
# 8. Immutable Tuple
# ------------------------------------------

numbers = (1, 2, 3)

print(numbers)

# This would cause an error:
#
# numbers[0] = 10
#
# Tuples are immutable.


# ------------------------------------------
# 9. == vs is
# ------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# True → same values

print(a is b)
# False → different objects


# ------------------------------------------
# 10. Mutable Example with Function
# ------------------------------------------

def add_number(numbers):

    numbers.append(100)


my_numbers = [1, 2, 3]

add_number(my_numbers)

print(my_numbers)

# Output:
# [1, 2, 3, 100]
#
# The function modified the original list
# because lists are mutable.


# ------------------------------------------
# 11. Immutable Example with Function
# ------------------------------------------

def change_number(number):

    number = 100


my_number = 10

change_number(my_number)

print(my_number)

# Output:
# 10
#
# The original integer did not change
# because integers are immutable.


# ==========================================
# QUICK SUMMARY
# ==========================================

# Mutable:
# list
# dictionary
# set
#
# Immutable:
# int
# float
# string
# tuple
# bool
#
# Mutable → object can be changed
# Immutable → object cannot be changed