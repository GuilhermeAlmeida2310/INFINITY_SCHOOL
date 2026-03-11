total = 0

for i in range(4):
    grade = float(input('Insert your grade: '))
    total += grade

gpa = total / 4

if gpa >= 6:
    print(f'Approved! - GPA: {gpa}')
else:
    print(f'Reproved! - GPA: {gpa}')