price = float(input('Insert price of product: '))
amount = int(input('Insert amount of product: '))

if amount >= 10:
    price -= price * 0.10
    print('You got the discount!')
else:
    print('You need to buy 10 items to get the discount!')

print(f'Total: ${price:.2f}')