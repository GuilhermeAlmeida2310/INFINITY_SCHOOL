number = int(input('Insert a integer: '))

if number > 0:
    if number % 2 == 0:
        print('The number is positive and even')
    else:
        print('The number is positive and odd')
elif number < 0:
    if number % 2 == 0:
        print('The number is negative and even')
    else:
        print('The number is negative and odd')
else:
    print('The number is zero')