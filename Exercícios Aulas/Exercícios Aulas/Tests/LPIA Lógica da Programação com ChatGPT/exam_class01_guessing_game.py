line = '-' * 30

num_fix = 8
attempts = 0

print('You have 3 attempts!')

while attempts < 3:
    number = int(input('Guess the number: '))
    attempts +=1

    if number == num_fix:
        print('You accept the number. Congratulations!')
        break
    
    else:
        print('Wrong guess! Try again!')
        print(line)

else:
    print('You ran out of attempts!')
