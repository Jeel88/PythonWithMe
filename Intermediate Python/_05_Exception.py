try:
    number = int(input("Enter number: "))
    result = 10 / number

    print(result)

except ValueError:
    print("You must enter a number")

except ZeroDivisionError:
    print("Cannot divide by zero")