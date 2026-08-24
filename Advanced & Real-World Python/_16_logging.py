import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.debug("Debug message")
logging.info("Program started")
logging.warning("Something might be wrong")
logging.error("Something went wrong")


def divide(a, b):
    logging.info("Dividing numbers")

    if b == 0:
        logging.error("Cannot divide by zero")
        return None

    result = a / b

    logging.info("Division completed")

    return result


print(divide(10, 2))
print(divide(10, 0))