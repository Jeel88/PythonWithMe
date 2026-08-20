numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)