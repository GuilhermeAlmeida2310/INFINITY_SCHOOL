numbers = []

amount = int(input('Insert the amount numbers: '))

for i in range(amount):
    number = float(input('Insert any number: '))
    numbers.append(number)

big_number = max(numbers)
small_number = min(numbers)
total = sum(numbers)

print(f'Biggest Number: {big_number}')
print(f'Smallest Number: {small_number}')
print(f'Total: {total:.2f}')