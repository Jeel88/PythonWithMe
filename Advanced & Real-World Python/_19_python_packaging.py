import sys


def show_package_info():
    print("Python version:", sys.version)
    print("Python executable:", sys.executable)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


show_package_info()

print(add(10, 20))
print(multiply(5, 4))