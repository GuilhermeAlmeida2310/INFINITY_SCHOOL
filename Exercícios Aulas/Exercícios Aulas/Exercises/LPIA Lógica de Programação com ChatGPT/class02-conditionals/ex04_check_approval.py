grade1 = float(input("Insert your first grade: "))
grade2 = float(input("Insert your second grade: "))

if grade1 >= 6 and grade2 >= 6:
    print("Both grades are 6 or higher!")
elif grade1 < 6 and grade2 < 6:
    print("Both grades are below 6!")
else:
    print("Only one of your grades is 6 or higher.")