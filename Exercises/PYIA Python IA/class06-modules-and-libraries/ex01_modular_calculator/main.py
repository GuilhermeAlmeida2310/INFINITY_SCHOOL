def number_sum(num1, num2):
    return f'Sum: {num1 + num2}'

def number_sub(num1, num2):
    return num1 - num2

def number_mult(num1, num2):
    return num1 * num2

def number_divi(num1, num2):
    if num2 == 0:
        return 'Insert the second number different of zero!'
    else:
        return num1 / num2