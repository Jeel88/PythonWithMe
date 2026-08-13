a = int(input("Enter First number: "))
b = int(input("Enter second number: "))
c = int(input("Enter Third number: "))
if a >=b and a >=c:
    largest =a
elif b>= a and b>= c:
    largest =b
else:
    largest =c
print("Largest Number is:",largest)