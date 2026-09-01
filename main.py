from decimal import Decimal

def get_number():
    while True:
        value = (input('Enter a number: '))
        try:
            number = float(value)
            break
        except ValueError:
            print('Please enter a number')
    return str(number)


def get_math_expression():
    while True:
        try:
            math_expression = input('Enter a math expression: ')
            if (math_expression == '+'
                    or math_expression == '-'
                    or math_expression == '*'
                    or math_expression == '/'):
                return math_expression
        except ValueError:
            print('Please enter a math expression')


def get_result(first_value, math_expression : str, second_value):
    while True:
        try:
            if math_expression == '+':
                return float(Decimal(first_value) + Decimal(second_value))
            elif math_expression == '-':
                return float(Decimal(first_value) - Decimal(second_value))
            elif math_expression == '*':
                return float(Decimal(first_value) * Decimal(second_value))
            elif math_expression == '/':
                return float(Decimal(first_value) / Decimal(second_value))
        except ValueError:
            print('Please enter a math expression')
