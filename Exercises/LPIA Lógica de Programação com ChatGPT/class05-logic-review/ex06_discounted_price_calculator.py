price_product = float(input('Insert the price of product: '))
discount = float(input('Insert the value of discount: '))

price_discount = price_product - (price_product * discount / 100)

print(f'Price with discount: ${price_discount:.2f}')