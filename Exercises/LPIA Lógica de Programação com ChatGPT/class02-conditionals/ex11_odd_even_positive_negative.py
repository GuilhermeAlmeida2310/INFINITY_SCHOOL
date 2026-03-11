num = int(input('Insert a number: '))

if num == 0:
    print('The number is zero!')
elif num %2 == 0 and num > 0:
    print('The number is even and positive!')
elif num %2 == 0:
    print('The number is even and negative!')
elif num %2 != 0 and num > 0:
    print('The number is odd and positive!')
else:
    print('The number is odd and negative!')