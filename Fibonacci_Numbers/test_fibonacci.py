import unittest
from Fibonacci_Numbers.Fibonacci import fib


class MyTestCase(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(6), 8)


if __name__ == '__main__':
    unittest.main()
