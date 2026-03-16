import random
import main

print('Try to hit the number than thinking machine 1 to 100')
secret_number = random.randint(1, 100)
attempts = 0


while True:
    number = int(input('Insert your guess: '))
    result = main.aleatory_number(number, secret_number)


    if number < 0:
        print('Insert a positive number!')
        continue

    else:
        if result == 'Biggest':
            print('Your guess is smaller than secret number!')
            attempts += 1
        
        elif result == 'Smaller':
            attempts += 1
            print('Your guess is biggest than secret number!')

        else:
            attempts += 1
            print('Congratulations! You to hit the number!')
            print(result)
            print(f'Attempts: {attempts}')
            break