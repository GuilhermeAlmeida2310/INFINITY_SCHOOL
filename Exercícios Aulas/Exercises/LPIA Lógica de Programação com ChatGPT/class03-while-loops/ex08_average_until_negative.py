total = 0
counter = 0
while True:
    grade = float(input('Insert the grade of students: '))
    if grade < 0:
        break
    total += grade
    counter += 1

average = total / counter

print(average)
