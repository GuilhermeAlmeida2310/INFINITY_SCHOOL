data = {
    'Name':'Gabriel',
    'Age': 25,
}

keys_list = ['Name','Age']

all_true = True

for i in keys_list:
    if i not in data:
        all_true = False
        
print(all_true)