list_01 = input('Insert a element in the first list: ').split()
list_02 = input('Insert a element in the second list: ').split()

result = set(list_01) | set(list_02)

print(f'Unique elements: {result}')