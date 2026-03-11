number = int(input('Insert a number for see the factorial: '))

if number > 0:
    factorial = 1
    counter = 1
    
    while counter <= number:
        factorial *= counter
        counter += 1

    print(f'The factorial of {number} is: {factorial}')
else:
    print('Not exist factorial for negative numbers!')