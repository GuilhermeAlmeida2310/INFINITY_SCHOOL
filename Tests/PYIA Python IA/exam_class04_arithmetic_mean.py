grades = []

def average_students(num1: float, num2: float, num3: float):
    average = (num1 + num2 + num3) / 3
    return average

for i in range(3):
    numbers = float(input('Insert your grade: '))
    grades.append(numbers)
print(average_students(grades[0], grades[1], grades[2]))