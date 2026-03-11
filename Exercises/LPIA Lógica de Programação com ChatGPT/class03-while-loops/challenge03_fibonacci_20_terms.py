term1 = 0
term2 = 1
counter = 1

while counter <= 20:
    print(term1)
    total = term1 + term2
    term1 = term2
    term2 = total
    counter += 1
