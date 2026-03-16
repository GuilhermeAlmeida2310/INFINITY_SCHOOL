number = int(input('Insert any number: '))
multiplier = 1

while multiplier <= 10:
    total = number * multiplier
    print(f'{number} X {multiplier} = {total}')
    multiplier += 1