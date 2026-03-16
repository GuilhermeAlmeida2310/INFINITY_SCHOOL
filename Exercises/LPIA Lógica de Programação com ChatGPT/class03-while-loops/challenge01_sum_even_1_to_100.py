total = 0
number = 1

while number <= 100:
    if number %2 == 0:
        total += number
    number += 1

print(f'Total Sum: {total}')