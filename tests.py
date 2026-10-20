import unittest
import model


class TestModel(unittest.TestCase):
    def test_addition(self):
        model.add_value('1')
        model.on_operator_pressed('+')
        model.add_value('2')
        self.assertEqual(model.get_result(), 3)

    def test_subtraction(self):
        model.add_value('1')
        model.on_operator_pressed('-')
        model.add_value('2')
        self.assertEqual(model.get_result(), -1)

    def test_multiplication(self):
        model.add_value('2')
        model.on_operator_pressed('×')
        model.add_value('4')
        self.assertEqual(model.get_result(), 8)

    def test_division(self):
        model.add_value('15')
        model.on_operator_pressed('÷')
        model.add_value('5')
        self.assertEqual(model.get_result(), 3)

    def test_reset(self):
        model.add_value('15')
        model.on_operator_pressed('÷')
        model.add_value('5')
        model.reset()
        self.assertEqual(model.current_operator, '')
        self.assertEqual(model.values, [])


if __name__ == '__main__':
    unittest.main()
