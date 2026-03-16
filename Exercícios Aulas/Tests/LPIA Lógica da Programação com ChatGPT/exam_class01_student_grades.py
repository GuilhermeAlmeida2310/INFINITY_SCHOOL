line = '-' * 20

grade_average = 0
number_students = int(input('Insert the students number: '))

for i in range(number_students):
    total = 0
    student_name = str(input('Student name: '))
    
    for i in range(3):
        grade = float(input('Insert the grade: '))
        total += grade
    average = total / 3
    grade_average += average

    print(line)
    print(f'Student: {student_name}')
    print(f'Average: {average:.2f}') 
    
    if average >= 7:
        print(f'Congratulations! {student_name} was approved!')
    
    else:
        print(f'{student_name} failed!')
    print(line)

class_average = grade_average / number_students

print('A média da turma é igual a ', class_average )