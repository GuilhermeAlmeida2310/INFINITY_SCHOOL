students = []

for i in range(5):
    name = input('Insert the student name: ')
    grade = float(input('Insert the student grade: '))
    students.append((name, grade))

best_student = max(students, key=lambda student: student[1])

print(f'Best Student: {best_student[0]} | Grade: {best_student[1]}')