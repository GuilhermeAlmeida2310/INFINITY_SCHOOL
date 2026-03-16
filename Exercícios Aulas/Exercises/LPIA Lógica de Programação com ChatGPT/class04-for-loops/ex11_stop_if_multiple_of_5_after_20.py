for i in range(1,31,1):
    if i >= 21:
        break
    else:
        if i %5 != 0:
            print(i)
        else:
            print(f'{i} - Multiple of 5')