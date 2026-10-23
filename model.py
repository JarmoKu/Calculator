from decimal import Decimal

values = []
current_operator = ''
operation_finished = False


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
            if operation_finished:
                reset()
                values.append(value)
                return
            values[1] += value
        case _:
            values.clear()


def add_decimal():
    match len(values):
        case 0:
            values[0] += '0.'
        case 1:
            values[0] += '.'
        case 2:
            values[1] += '.'
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
    global operation_finished
    operation_finished = True
    first_value = Decimal(values[0])
    second_value = Decimal(values[1])
    match current_operator:
        case '+':
            return float(Decimal(first_value) + Decimal(second_value))
        case '-':
            return float(Decimal(first_value) - Decimal(second_value))
        case '×':
            return float(Decimal(first_value * second_value))
        case '÷':
            return float(Decimal(first_value / second_value))
        case _:
            return 0


def reset():
    global values
    global current_operator
    global operation_finished
    operation_finished = False
    values.clear()
    current_operator = ''
