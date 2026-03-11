total = 0

amount = int(input('Insert the number of people will be verificarion: '))

for i in range(amount):
    age = int(input('Insert the age: '))
    total += age

average = total / amount

if 0 < average <= 25:
    print('Young Class')
elif 25 < average <= 59:
    print('Adult Class')
elif 60 <= average <= 120:
    print('Elderly Class')
else:
    print('Insert valid ages!')