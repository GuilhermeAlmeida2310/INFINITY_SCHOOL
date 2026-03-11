number = int(input('Insert a number: '))

while number >= 10:
    total = 0
    
    while number > 0:
        total = total + (number % 10)
        number = number // 10
    number = total

print(f'Result: {number}')