def aleatory_number(number,secret_number):
    if number > secret_number:
        return 'Biggest'
    elif number < secret_number:
        return 'Smaller'
    else:
        return number, secret_number