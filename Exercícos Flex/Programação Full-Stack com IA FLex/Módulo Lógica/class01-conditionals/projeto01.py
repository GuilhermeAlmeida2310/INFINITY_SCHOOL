grade1 = float(input('Insert first grade: '))
grade2 = float(input('Insert second grade: '))
grade3 = float(input('Insert third grade: '))

gpa = (grade1 + grade2 + grade3) / 3

if gpa >= 7:
    print('Approved!')
elif gpa >= 5:
    print('Recovery!')
else:
    print('Reproved!')