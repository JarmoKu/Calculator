import unittest
from main import get_result

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(get_result('1.1', '+', '2'), 3.1)

    def test_subtraction(self):
        self.assertEqual(get_result('2.1', '-', '3'), -0.9)

    def test_multiplication(self):
        self.assertEqual(get_result('1.2', '*', '3'), 3.6)

    def test_division(self):
        self.assertEqual(get_result('15', '/', '3'), 5.0)


if __name__ == '__main__':
    unittest.main()
