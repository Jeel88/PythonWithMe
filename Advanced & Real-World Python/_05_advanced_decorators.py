from functools import wraps


def log_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return wrapper


@log_function
def add(a, b):
    return a + b


print(add(5, 3))


def check_age(func):

    @wraps(func)
    def wrapper(age):
        if age >= 18:
            return func(age)

        return "Access denied"

    return wrapper


@check_age
def enter(age):
    return "Access granted"


print(enter(20))
print(enter(15))


def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello(name):
    print("Hello", name)


hello("Jeel")