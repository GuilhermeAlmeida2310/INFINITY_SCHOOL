users = {}

amount = int(input('Insert the quantity of people that will registered: '))

for i in range(amount):
    user = input('Insert the people name: ')
    password = str(input('Insert your password: '))
    users[user] = password

print(users)

while True:
    name = input('Insert your username: ')

    if name in users:
        print('User found in database!')
        login = input('Insert your password: ')
        
        if login == users[name]:
            print(f'Welcome to back {name}!')
            break
         
        else:
            print('Incorrect Password!')

    else:
        print('This person is not registered!')