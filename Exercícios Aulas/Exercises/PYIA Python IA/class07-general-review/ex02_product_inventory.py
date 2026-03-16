line = '-' * 50

store_stock = []

def add_product():
    product = input('Insert the product name: ')
    price = float(input('Insert the price of product: '))
    amount = int(input('Insert the amount of product: '))

    store_stock.append({'Product':product.capitalize(), 'Price':price, 'Amount':amount})
    print(f'{product} has been added to the store!')
    print(line)

def remove_product():
    product = input('Insert the product name: ')
    product = product.capitalize()

    product_found = None
    for item in store_stock:
        if item['Product'] == product:
            product_found = item
            break
    
    if product_found is None:
        print('This product is not in our store!')
        print(line)

    else:
        store_stock.remove(product_found)
        print(f'{product} has been removed from the store!')
        print(line)

def product_update():
    product = input('Insert the product name: ')
    product = product.capitalize()

    product_index = -1
    for i in range(len(store_stock)):
        if store_stock[i]['Product'] == product:
            product_index = i
            break

    if product_index == -1:
        print('This product is not in our store!')
        print(line)

    else:
        while True:
            print('===== OPTIONS =====')
            print('1. Update Product Name')
            print('2. Update Product Price')
            print('3. Update Product Amount')
            print('4. Exit')

            option = int(input('Choose an option: '))

            if option == 1:
                new_product = input('Insert the new product name: ')
                old_name = store_stock[product_index]['Product']
                store_stock[product_index]['Product'] = new_product.capitalize()

                print('Products catalog updated successfully!')
                print(f'The old product name: {old_name}')
                print(f'The new product name: {new_product}')
                print(line)

            elif option == 2:
                new_price = float(input('Insert the new product price: '))
                old_price = store_stock[product_index]['Price']
                store_stock[product_index]['Price'] = new_price

                print('The products catalog was updated!')
                print(f'The old product price: ${old_price:.2f}')
                print(f'The new product price: ${new_price:.2f}')
                print(line)

            elif option == 3:
                new_amout = int(input('Insert the new product quantity: '))
                old_amount = store_stock[product_index]['Amount']
                store_stock[product_index]['Amount'] = new_amout

                print('The products catalog was updated!')
                print(f'The old product amount: {old_amount}')
                print(f'The new product amount: {new_amout}')
                print(line)

            elif option == 4:
                print('Exiting update menu...')
                print(line)
                break

            else:
                print('Please enter a valid option!')
                continue

def look_products():
    for i, product in enumerate(store_stock, start=1):
        print(f'{i} | Product: {product['Product']} | Price: ${product['Price']:.2f} | Amount: {product['Amount']}')
    print(line)

def menu():
    while True:
        print('===== STORE STOCK =====')
        print('1. Add Product')
        print('2. Remove Product')
        print('3. Update Product')
        print('4. Look Products List')
        print('5. Exit')

        option = int(input('Choose an option: '))

        if option == 1:
            add_product()

        elif option == 2:
            remove_product()

        elif option == 3:
            product_update()

        elif option == 4:
            look_products()

        elif option == 5:
            print('Exiting program. Goodbye!')
            break

        else:
            print('Please enter a valid option!')
            continue

menu()