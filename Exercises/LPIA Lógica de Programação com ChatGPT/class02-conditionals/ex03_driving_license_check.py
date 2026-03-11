age = int(input("Insert your age: "))
license = int(input("Do you have a driver's license? 1-)Yes | 2-)No: "))

if age >= 18 and license == 1:
    print("You are authorized to drive.")
elif age >= 18 and license == 2:
    print("You are old enough to drive, but you don't have a license.")
else:
    print("You are neither old enough nor have a license to drive.")