secret_number = 50
attempts = 0

while True:
    number = int(input('Try to guess the number between 1 and 100: '))
    
    if number > secret_number:
        print('Your guess is bigger than correct number!')
        attempts += 1
    elif number < secret_number:
        print('Your guess is smaller than correct number!')
        attempts += 1
    else:
        print('You win. Congratulations!')
        print(f'Attempts: {attempts}')
        break