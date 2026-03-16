correct_user = 'Python'
correct_password = '1991'

while True:
    user = input('Insert your name of user: ')
    password = input('Insert your password: ')

    if user == correct_user and password == correct_password:
        print('Access grated. Welcome!')
        break
    else:
        print('Incorrect user or password!')
        continue