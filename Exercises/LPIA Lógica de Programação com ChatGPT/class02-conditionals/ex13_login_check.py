user = input('Insert your name user: ')
password = input('Insert your password: ')

if user == 'admin' and password == '1234':
    print('Access granted! Welcome!')
else:
    print('Access block!')