def calculator(num1, num2, operator):
    if operator == '+':
        calculation = lambda x, y: x + y
    
    elif operator == '-':
        calculation = lambda x, y: x - y
    
    elif operator == '*':
        calculation = lambda x, y: x * y

    elif operator == '/':
        if num2 == 0:
            return 'Insert a number different of zero!'
        calculation = lambda x, y: x / y

    else:
        return 'Insert a valid operator!'

    print(calculation(num1, num2))
    return calculation(num1, num2)

calculator(5, 5, '+')