weight = float(input('Insert your weight: '))
height = float(input('Insert your height: '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('You are underweight')
elif 18.5 <= bmi <= 24.9:
    print('You have a normal weight')
elif 25 <= bmi <= 29.9:
    print('You are overweight')
else:
    print('You are obese')