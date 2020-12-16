import unittest
from Can_Sum_Problem.Can_Sum import canSum


class MyTestCase(unittest.TestCase):
    def test_short(self):
        message = "Test value is not true."
        self.assertTrue(canSum(7, [2, 3]), message)          # True
        self.assertTrue(canSum(7, [5, 3, 4, 7]), message)    # True
        self.assertFalse(canSum(7, [2, 4]), message)         # False
        self.assertTrue(canSum(8, [2, 3, 5]), message)       # True

    def test_long(self):
        message = "Test value is not False."
        self.assertFalse(canSum(300, [7, 14]), message)      # False


if __name__ == '__main__':
    unittest.main()
