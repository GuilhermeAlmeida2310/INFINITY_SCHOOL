data = {'Lucas':19}

amount = int(input('Insert how many names and ages you want add in dict: '))

for i in range(amount):
    name = input('Insert a name: ')
    age = int(input('Insert age: '))
    data[name] = age

print(data)