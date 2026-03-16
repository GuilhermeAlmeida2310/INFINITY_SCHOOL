students = {
    'Guilherme':10,
    'Camila':9,
    'Victor':7.5,
    'Beatriz':8.5,
    'Arthur':10
}

sum_grades = 0
for name, grade in students.items():
    sum_grades += grade

average = sum_grades / len(students)

print(f'Students Average: {average}')

name = input('Insert the student name for search: ')

for names, grade in students.items():
    if name == names:
        print(f'Grade of: {name}: {grade}')
        break
else:
    print('Student not found!')