while True:
    number = int(input('Insert a number of 1 to 10: '))
    if number > 10 or number < 0:
        print('Insert a valid option!')
        continue
    else:
        print('Thanks!')
        break