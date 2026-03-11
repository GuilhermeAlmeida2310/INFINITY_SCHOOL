correct_password = 'Python'

while True:
    password = input('Insert the password: ')
    if password == correct_password:
        print('Access Granted. Welcome!')
        break
    else:
        print('Access Denied!')
        continue