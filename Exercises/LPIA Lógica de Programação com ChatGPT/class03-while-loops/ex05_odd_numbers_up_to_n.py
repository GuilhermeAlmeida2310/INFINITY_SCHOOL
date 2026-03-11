number = int(input('Insert any number: '))
counter = 0

while counter < number:
    counter += 1
    if counter %2 != 0:
        print(counter)