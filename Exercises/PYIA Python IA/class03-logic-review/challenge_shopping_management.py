products = {}
total_price = 0
thousand = 0

amount = int(input('Insert the number of products than you want add: '))

for i in range(amount):
    product = input('Insert the name of product: ')
    price = float(input('Insert the price of product: '))
    total_price += price
    products[product] = price

    if price > 1000:
        thousand += 1

small_price = min(products.values())

print(f'Total Price: R${total_price:.2f}')
print(f'Amount products more than thousand: {thousand}')

for name, value in products.items():
    if value == small_price:
        print(f'Cheaper product: {name} - ${value:.2f}')
        break