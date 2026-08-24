def outer():
    message = "Hello Jeel"

    def inner():
        print(message)

    return inner


greet = outer()

greet()