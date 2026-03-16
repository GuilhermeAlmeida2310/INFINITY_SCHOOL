from functools import reduce

def find_biggest_str(list_strings):
    biggest = reduce(lambda x, y: x if len(x) > len(y) else y, list_strings)
    return biggest

words = ['Dog', 'Cat', 'Bird', 'Rabbit']

result = find_biggest_str(words)

print(f'The biggest word is: {result}')