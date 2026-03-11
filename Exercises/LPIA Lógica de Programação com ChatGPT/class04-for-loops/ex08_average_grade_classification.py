total = 0

for i in range(5):
    grade = float(input('Insert your grade: '))
    total += grade

average = total / 5

if average >= 6:
    print('You were approved!')
else:
    print('You were reproved!') 