import unittest


def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_even(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(7))

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()