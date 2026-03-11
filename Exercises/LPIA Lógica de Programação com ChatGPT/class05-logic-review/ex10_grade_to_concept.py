while True:
    grade = int(input('Insert your grade: '))

    if grade == 100:
        print('Grade: A')
        break
    elif grade >= 75 and grade < 100:
        print('Grade: B')
        break
    elif grade >= 50 and grade < 75:
        print('Grade: C')
        break
    elif grade >= 25 and grade < 50:
        print('Grade: D')
        break
    elif grade < 25 and grade >= 0:
        print('Grade: F')
        break
    else:
        print('Insert a grade between 0 and 100!')
        continue