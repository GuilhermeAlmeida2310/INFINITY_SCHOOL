evens = 0
odd = 0

for i in range(10):
    number = int(input('Insert a number: '))

    if number %2 == 0:
        evens += 1
    else:
        odd += 1


print(f'Even Numbers: {evens}')
print(f'Odd Numbers: {odd}')