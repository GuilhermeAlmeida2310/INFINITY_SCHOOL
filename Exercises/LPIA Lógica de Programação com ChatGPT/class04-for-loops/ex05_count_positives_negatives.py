positives = 0
negatives = 0

for i in range(10):
    number = int(input('Insert a number: '))

    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
    else:
        print("Number zero can't be inserted!")
        while True:
            number = int(input('Insert a number: '))
            if number > 0:
                positives += 1
                break
            elif number < 0:
                negatives += 1
                break
            else:
                print("Number zero can't be inserted!")
                continue

print(f'Positives Numbers: {positives} | Negative Numbers: {negatives}')