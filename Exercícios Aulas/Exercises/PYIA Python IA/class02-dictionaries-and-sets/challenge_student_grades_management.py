students = []
averages = []
line = '=' * 30

while True:
    print('1. Registrer of Students')
    print('2. Show Students')
    print('3. Average of Grades')
    print('4. Student with Best Average')
    print('5. Exit')

    option = int(input('Choose an option: '))

    if option == 1:
        student_name = input('Insert the student name: ')
        student_age = int(input('Insert the student age: '))
        grade_math = float(input('Insert the math grade: '))
        grade_science = float(input('Insert the science grade: '))
        grade_history = float(input('Insert the history grade: '))
        students.append({'Student':student_name,'Age':student_age,'Grades':(grade_math,grade_science,grade_history)})
        print(f'The student {student_name} was registered successfully')
        print(line)

    elif option == 2:
        print('Students Registred:')
        for show_student in students:
            print(show_student)
        print(line)

    elif option == 3:
        if not students:
            print('No grades registered! Registrer students first.')
            continue
        else:
            for student in students:
                sum_grades = 0
                grade = student['Grades']
                for i in grade:
                    sum_grades += i
                average = sum_grades / len(grade)
                averages.append(average)
                print(f"{student['Student']} - Average: {average:.2f}")
            print(line)

    elif option == 4:
        if not students:
            print('No students registered!')
            print('='*30)
            continue
        else:
            best_average = max(averages)
            for i, avg in enumerate(averages):
                if avg == best_average:
                    print(f"Student: {students[i]['Student']} | Average: {best_average:.2f}")
            print(line)

    elif option == 5:
        print('Closing the program. See you later!')
        break

    else:
        print('Insert a valid option please!')
        print(line)
        continue
