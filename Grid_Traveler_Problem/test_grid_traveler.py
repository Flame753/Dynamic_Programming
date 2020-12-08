import unittest
from Grid_Traveler_Problem.Grid_Traveler import grid_traveler as gridT


class MyTestCase(unittest.TestCase):
    def test_paths(self):
        self.assertEqual(gridT(1, 1), 1)
        self.assertEqual(gridT(1, 0), 0)
        self.assertEqual(gridT(0, 1), 0)
        self.assertEqual(gridT(0, 0), 0)
        self.assertEqual(gridT(8, 0), 0)
        self.assertEqual(gridT(2, 3), 3)


if __name__ == '__main__':
    unittest.main()
