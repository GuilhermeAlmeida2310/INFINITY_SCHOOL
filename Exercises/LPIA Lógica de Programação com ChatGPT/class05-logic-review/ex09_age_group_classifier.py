age = int(input('Insert your age: '))

if age < 10:
    print('You are a child!')
elif age >= 10 and age < 20:
    print('You are a adolescent!')
elif age >= 20 and age < 60:
    print('You are a adult!')
elif age >= 60 and age <= 125:
    print('You are a elderly!')
else:
    print('Impossible!')