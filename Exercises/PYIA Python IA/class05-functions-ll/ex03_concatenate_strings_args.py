def concatenate_strings(*args):
    result = ''
    for string in args:
        result += string
    return result

print(concatenate_strings('Juice','fruit'))