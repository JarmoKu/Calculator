from decimal import Decimal

values = []
current_operator = ''


def add_value(value):
    match len(values):
        case 0:
            values.append(value)
        case 1:
            if current_operator != '':
                values.append(value)
                return
            values[0] += value
        case 2:
            if current_operator != '':
                reset()
                values.append(value)
                return
            values[1] += value
        case _:
            values.clear()


def on_operator_pressed(operator):
    global current_operator
    if len(values) == 2 and current_operator != '':
        result = get_result()
        reset()
        add_value(result)

    current_operator = operator


def get_result():
    first_value = Decimal(values[0])
    second_value = Decimal(values[1])
    match current_operator:
        case '+':
            return float(Decimal(first_value) + Decimal(second_value))
        case '-':
            return float(Decimal(first_value) - Decimal(second_value))
        case 'x':
            return float(Decimal(first_value * second_value))
        case '%':
            return float(Decimal(first_value / second_value))
        case _:
            return 0


def reset():
    global values
    global current_operator
    values.clear()
    current_operator = ''
