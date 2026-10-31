from decimal import Decimal

values = []
current_operator = ''
final_result: int | None = None


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
            if final_result is not None:
                reset()
                values.append(value)
                return
            values[1] += value
        case _:
            raise ValueError(f'More values than allowed: {len(values)}')


def sign_change():
    global final_result
    if final_result is not None:
        reset_and_toggle_result_negative(final_result)
        return
    value_count = len(values)
    match value_count:
        case 0:
            values.append('-0')
        case 1:
            toggle_operand_negative(value_count)
        case 2:
            toggle_operand_negative(value_count)
        case _:
            raise ValueError(f'More values than allowed: {len(values)}')


def toggle_operand_negative(value_count):
    last_value = values[value_count - 1]
    if last_value.count('-') == 0:
        values[value_count - 1] = '-' + last_value
    else:
        values[value_count - 1] = last_value.replace('-', '')


def reset_and_toggle_result_negative(result):
    temp = -result
    reset()
    values.append(temp)


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
        calculate_result()
        temp_result = final_result
        reset()
        add_value(temp_result)
    current_operator = operator


def calculate_result():
    global final_result
    if len(values) == 0:
        values.append('0')
        final_result = 0
    first_value = Decimal(values[0])
    if len(values) == 1:
        if current_operator == '':
            final_result = first_value
        else:
            final_result = binary_operation(first_value, first_value)
    second_value = first_value if len(values) == 1 else Decimal(values[1])
    final_result = binary_operation(first_value, second_value)


def get_result():
    return final_result


def binary_operation(first_operand, second_operand):
    match current_operator:
        case '+':
            return float(Decimal(first_operand + second_operand))
        case '-':
            return float(Decimal(first_operand - second_operand))
        case '×':
            return float(Decimal(first_operand * second_operand))
        case '÷':
            return float(Decimal(first_operand / second_operand))
        case _:
            return first_operand


def reset():
    global values
    global current_operator
    global final_result
    final_result = None
    values.clear()
    current_operator = ''
