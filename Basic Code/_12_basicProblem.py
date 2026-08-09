#odd even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#positive negative
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#multiplication table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")    

#sum in loop
number = int(input("Enter a number: "))
total = 0
for i in range(1, number + 1):
    total += i
print("Sum:", total)    