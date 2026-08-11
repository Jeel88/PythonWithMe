numbers=[1,2,3,4,5]
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)
print(even_numbers)