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
            raise ValueError(f'More values than allowed: {len(values)}')


def toggle_negative():
    value_count = len(values)
    if value_count == 0:
        values.append('-0')
    elif value_count == 1 or value_count == 2:
        if values[value_count - 1].count('-') == 0:
            values[value_count - 1] = '-' + values[value_count - 1]
        else:
            values[value_count - 1] = values[value_count - 1].replace('-', '')
    else:
        raise ValueError(f'More values than allowed: {len(values)}')


def add_decimal():
    match len(values):
        case 0:
            values.append('0.')
        case 1:
            if current_operator != '':
                values.append('0.')
            elif values[0].count('.') == 0:
                values[0] += '.'
        case 2:
            if values[1].count('.') == 0:
                values[1] += '.'
        case _:
            raise ValueError(f'More values than allowed: {len(values)}')


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
    if len(values) == 0:
        values.append('0')
        return 0
    elif len(values) == 1:
        if current_operator == '':
            return Decimal(values[0])
    first_value = Decimal(values[0])
    second_value = first_value if len(values) == 1 else Decimal(values[1])
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
            raise ValueError(f'Not a valid operator: {current_operator}')


def reset():
    global values
    global current_operator
    global operation_finished
    operation_finished = False
    values.clear()
    current_operator = ''
