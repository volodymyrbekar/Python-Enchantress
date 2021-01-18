import unittest
from homework.test_simple_calc import add, subtract, multiply, divide


class TestAssets(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 5), 9)

    def test_subtract(self):
        self.assertEqual(subtract(6, 5), 1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)


if __name__ == "__main__":
    unittest.main()
