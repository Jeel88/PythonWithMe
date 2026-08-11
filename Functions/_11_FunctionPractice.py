def even(n):
    if n%2==0:
        print("even ",n)
even(4)
even(5)        

def maximum(a,b):
    if a > b:
        return a
    return b
print(maximum(10, 20))

def calculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(calculate_sum(10, 20))
print(calculate_sum(1, 2, 3, 4, 5))

def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)
student_info(
    name="Jeel",
    age=20,
    course="BTech IT"
)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial:", factorial(5))