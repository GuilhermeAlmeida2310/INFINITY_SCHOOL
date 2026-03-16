def create_shop_list(*args):
    return args

shop_list = []
amount = int(input('Insert amount of products in list: '))

for i in range(amount):
    product = input('Insert the name of product: ')
    shop_list.append(product)

result = create_shop_list(*shop_list)

print(result)