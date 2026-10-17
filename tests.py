import unittest
import model


class TestModel(unittest.TestCase):
    def test_addition(self):
        model.current_operator = '+'
        model.values = ['1.1', '2']
        self.assertEqual(model.get_result(), 3.1)

    def test_subtraction(self):
        model.current_operator = '-'
        model.values = ['2.1', '3']
        self.assertEqual(model.get_result(), -0.9)

    def test_multiplication(self):
        model.current_operator = 'x'
        model.values = ['1.2', '3']
        self.assertEqual(model.get_result(), 3.6)

    def test_division(self):
        model.current_operator = '%'
        model.values = ['15', '3']
        self.assertEqual(model.get_result(), 5.0)


if __name__ == '__main__':
    unittest.main()
