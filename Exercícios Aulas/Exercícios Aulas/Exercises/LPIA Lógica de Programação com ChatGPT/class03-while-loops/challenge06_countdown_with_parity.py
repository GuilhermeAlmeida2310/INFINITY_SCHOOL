number = int(input('Insert a number: '))

counter = number

while counter >= 0:
    if counter %2 == 0:
        print(f'{counter} - Even number')
    else:
        print(counter)        

    counter -= 1
