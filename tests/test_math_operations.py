import unittest
from factorial.math_operations import factorial, factorial_recursive


class TestFactorial(unittest.TestCase):
    def test_minus_1(self):
        self.assertEqual(factorial(-1), 'Only natural numbers!')

    def test_0(self):
        self.assertEqual(factorial(0), 1)

    def test_1(self):
        self.assertEqual(factorial(1), 1)

    def test_2(self):
        self.assertEqual(factorial(2), 2)

    def test_3(self):
        self.assertEqual(factorial(3), 6)

    def test_5(self):
        self.assertEqual(factorial(5), 120)

    def test_recursive_minus_1(self):
        self.assertEqual(factorial_recursive(-1), 'Only natural numbers!')

    def test_recursive_0(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_recursive_1(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_recursive_2(self):
        self.assertEqual(factorial_recursive(2), 2)

    def test_recursive_3(self):
        self.assertEqual(factorial_recursive(3), 6)

    def test_recursive_5(self):
        self.assertEqual(factorial_recursive(5), 120)


if __name__ == "__main__":
    unittest.main()
