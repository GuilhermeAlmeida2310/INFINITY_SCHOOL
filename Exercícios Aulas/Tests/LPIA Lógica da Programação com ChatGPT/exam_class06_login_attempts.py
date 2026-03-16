user = 'Python'
password = '1991'
attempts = 3

for i in range(3):

    confirm_name = input('Confirm your username: ')
    confirm_password = input('Confirm your password: ')
    
    if confirm_name == user and confirm_password == password:
        print('Access granted! Welcome.')
        break

    else:
        attempts -= 1
        print('Incorrect username or password')
        print(f'Remaining Attempts:{attempts}')

else:
    print('Access failed!')