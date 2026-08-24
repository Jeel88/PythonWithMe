name: str = "Jeel"
age: int = 20
price: float = 99.99
is_student: bool = True

print(name)
print(age)
print(price)
print(is_student)


def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))


def greet(name: str) -> str:
    return f"Hello {name}"


print(greet("Jeel"))


def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))


def get_student() -> dict[str, int]:
    return {
        "age": 20
    }


print(get_student())


def find_name(names: list[str], name: str) -> bool:
    return name in names


print(find_name(["Jeel", "Aman", "Rahul"], "Jeel"))


def process(value: int | str) -> None:
    print(value)


process(10)
process("Python")