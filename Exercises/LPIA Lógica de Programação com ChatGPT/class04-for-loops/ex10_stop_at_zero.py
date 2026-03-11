positives = 0
negatives = 0

for i in range(10):
    number = int(input('Insert a number (Insert 0 for stop): '))

    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
    else:
        print('Exiting loop...')
        break

print(f'Positives Numbers: {positives} | Negative Numbers: {negatives}')