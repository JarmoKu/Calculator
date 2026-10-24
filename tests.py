import unittest
import model

test_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
test_operators = ['+', '-', '×', '÷']

class TestModel(unittest.TestCase):
    def test_addition(self):
        result = self.calculate(['1', '+', '2'])
        self.assertEqual(result, 3)
        model.reset()

    def test_subtraction(self):
        result = self.calculate(['1', '-', '2'])
        self.assertEqual(result, -1)
        model.reset()

    def test_multiplication(self):
        result = self.calculate(['2', '×', '4'])
        self.assertEqual(result, 8)
        model.reset()

    def test_division(self):
        result = self.calculate(['1', '5', '÷', '5'])
        self.assertEqual(result, 3)
        model.reset()

    def test_reset(self):
        self.use_test_input(['1', '5', '÷', '5'])
        model.reset()
        self.assertEqual(model.current_operator, '')
        self.assertEqual(model.values, [])

    def test_decimal_added(self):
        result = self.calculate(['2', '.', '1', '+', '4', '.', '2'])
        self.assertEqual(model.values, ['2.1', '4.2'])
        self.assertEqual(result, 6.3)
        model.reset()

    def test_toggle_negative(self):
        self.use_test_input(['+/-'])
        self.assertEqual(model.values[0], '-0')
        self.use_test_input(['+/-'])
        self.assertEqual(model.values[0], '0')
        model.reset()

    def test_toggle_negative_first_value(self):
        self.use_test_input(['2', '4', '+/-'])
        self.assertEqual(model.values[0], '-24')
        self.use_test_input(['+/-'])
        self.assertEqual(model.values[0], '24')
        model.reset()

    def test_toggle_negative_second_value(self):
        self.use_test_input(['2', '+', '4', '+/-'])
        self.assertEqual(model.values[1], '-4')
        self.use_test_input(['+/-'])
        self.assertEqual(model.values[1], '4')
        model.reset()

    def test_toggle_negative_addition(self):
        result = self.calculate(['5', '+/-', '+', '3'])
        self.assertEqual(result, -2)
        model.reset()

    def test_toggle_negative_substraction(self):
        result = self.calculate(['2', '4', '-', '5', '6', '+/-'])
        self.assertEqual(result, 80)
        model.reset()

    def test_toggle_negative_multiplication(self):
        result = self.calculate(['2', '×', '5', '+/-'])
        self.assertEqual(result, -10)
        model.reset()

    def test_toggle_negative_division(self):
        result = self.calculate(['1', '5', '÷', '5', '+/-'])
        self.assertEqual(result, -3)
        model.reset()

    @staticmethod
    def use_test_input(test_inputs):
        for test_input in test_inputs:
            if test_input in test_values:
                model.add_value(test_input)
                continue
            if test_input == '.':
                model.add_decimal()
                continue
            if test_input == '+/-':
                model.toggle_negative()
                continue
            if test_input in test_operators:
                model.on_operator_pressed(test_input)
                continue

    def calculate(self, test_inputs):
        self.use_test_input(test_inputs)
        return model.get_result()

if __name__ == '__main__':
    unittest.main()
