line = '-' * 30

def number_sum():
    num1 = float(input('Insert the first number: '))
    num2 = float(input('Insert the second number: '))
    print(f'Result: {num1 + num2}')
    print(line)
    return num1 + num2

def number_sub():
    num1 = float(input('Insert the first number: '))
    num2 = float(input('Insert the second number: '))
    print(f'Result: {num1 - num2}')
    print(line)
    return num1 - num2

def number_mult():
    num1 = float(input('Insert the first number: '))
    num2 = float(input('Insert the second number: '))
    print(f'Result: {num1 * num2}')
    print(line)
    return num1 * num2

def number_divi():
    num1 = float(input('Insert the first number: '))
    num2 = float(input('Insert the second number: '))

    if num2 == 0:
        print('Insert the second number different of zero!')
    else:
        print(f'Result: {num1 / num2}')
        print(line)
        return num1 / num2

def menu():
    while True:
        print('1. Add Numbers')
        print('2. Subtract Numbers')
        print('3. Multiply Numbers')
        print('4. Dividing Numbers')
        print('5. Exit')

        option = int(input('Insert a option: '))

        if option == 1:
            number_sum()

        elif option == 2:
            number_sub()
        
        elif option == 3:
            number_mult()
        
        elif option == 4:
            number_divi()

        elif option == 5:
            print('Exiting...')
            break

        else:
            print('Insert a valid option please!')
            print(line)
            continue

menu()