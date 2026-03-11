def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

g1 = float(input('Insert the first grade: '))
g2 = float(input('Insert the second grade: '))
g3 = float(input('Insert the third grade: '))

average = calculate_average(g1, g2, g3)

print(f'Average: {average}')