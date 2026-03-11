correct_user = 'Python'
correct_password = '1991'
attempts = 0

while attempts < 3:
    user = input('Insert your name of user: ')
    password = input('Insert your password: ')
    attempts += 1

    if user == correct_user and password == correct_password:
        print(f'Number of attempts: {attempts}')
        print('Access granted. Welcome!')
        break
    else:
        if attempts == 3:
            print('Incorrect user or password. Access Denied!')
            print(f'Number of attempts: {attempts}')
            break
        else:
            print('Incorrect user or password. Try again!')
            print(f'Number of attempts: {attempts}')