total = 0
discount = 10

for i in range(5):
    price = float(input('Insert the price of product: '))

    total += price

    if total > 100:
        break

price_discount = total - (total * discount / 100)

print(f'Price with discount: ${price_discount:.2f}')
