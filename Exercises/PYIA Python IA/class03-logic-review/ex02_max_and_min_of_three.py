numbers = []

for i in range(3):
    number = int(input('Insert a number: '))
    numbers.append(number)

big_number = max(numbers)
small_number = min(numbers)

print(f'Biggest Number: {big_number}')
print(f'Smallest Number: {small_number}')