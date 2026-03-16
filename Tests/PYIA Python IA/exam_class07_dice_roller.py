import random

numbers = [1, 2, 3, 4, 5, 6]

def launch_dice():
    die1 = random.choice(numbers)
    die2 = random.choice(numbers)
    result = die1 + die2

    print(f'First Die: {die1}')
    print(f'Second Die: {die2}')
    print(f'Sum of dice values: {result}')

launch_dice()