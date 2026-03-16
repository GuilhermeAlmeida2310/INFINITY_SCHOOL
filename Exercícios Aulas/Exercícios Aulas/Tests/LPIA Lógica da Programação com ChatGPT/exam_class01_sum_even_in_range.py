start = int(input('Insert a start number: '))
end = int(input('Insert a end number: '))
total = 0

for number in range(start, end + 1):
    if number % 2 == 0:
        total += number

if total > 0:    
    print(f'The sum of even numbers is: {total}') 
else:
    print('None even number was inserted!')