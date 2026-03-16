number = int(input('Insert any number: '))
multiplier = 1

while multiplier <= 10:
    total = number * multiplier
    if total %3 == 0:
        print(f'{number} X {multiplier} = {total}')
    multiplier += 1
