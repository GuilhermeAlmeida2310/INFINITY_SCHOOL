number = int(input('Insert a number for see the multiplication table: '))

for i in range(1,11,1):
    total = number * i
    print(f'{number} X {i} = {total}')