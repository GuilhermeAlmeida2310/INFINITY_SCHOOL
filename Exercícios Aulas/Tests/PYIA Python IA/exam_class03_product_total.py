products = {}
total = 0

while True:
    print('Do you want to add products to the catalog?')
    print('1. Yes')
    print('2. No')

    option = int(input('Choose an option: '))

    if option == 1:
        amount = int(input('Insert how many products you want to include: '))

        for i in range(amount):
            if amount > 0:
                product = input('Insert the product name: ')
                price = float(input('Insert the product price: '))
                products[product] = price

    elif option == 2:
        print('Exiting program...')
        break

    else:
        print('Please choose a valid option!')
        continue

for key, value in products.items():
    total += value

print(f'Total: ${total:.2f}')