total = 0

while True:
    number = int(input('Insert any positive number (Insert a negative number for stop): '))
    if number < 0:
        break
    else:
        total += number

print(f'Total Sum: {total}')