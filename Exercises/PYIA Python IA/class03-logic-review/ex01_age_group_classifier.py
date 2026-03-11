age = int(input('Insert a age: '))

if age < 12:
    print('Child')
elif age >= 12 and age <= 17:
    print('Adolescent')
elif age >= 18 and age <= 59:
    print('Adult')
elif age >= 60 and age < 120:
    print('Elderly')
else:
    print('Invalid age!')