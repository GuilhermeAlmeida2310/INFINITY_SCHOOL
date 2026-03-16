student1_grade1 = float(input('Insert the first grade of first student: '))
student1_grade2 = float(input('Insert the second grade of first student: '))
average_student1 = (student1_grade1 + student1_grade2) / 2

if average_student1 >= 7:
    print('First student was approved!')
elif average_student1 >= 5:
    print('First student is in recovery!')
else:
    print('First student was reproved!')

student2_grade1 = float(input('Insert the first grade of second student: '))
student2_grade2 = float(input('Insert the second grade of second student: '))
average_student2 = (student2_grade1 + student2_grade2) / 2

if average_student2 >= 7:
    print('Second student was approved!')
elif average_student2 >= 5:
    print('Second student is in recovery!')
else:
    print('Second student was reproved!')