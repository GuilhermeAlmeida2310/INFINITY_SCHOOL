age = int(input('Insert your age: '))
driver_license = int(input("Do you have a driver's license? 1-)Yes | 2-)No: "))

if age >= 18 and driver_license == 1:
    print('You can drive')
else:
    print("You can't drive")