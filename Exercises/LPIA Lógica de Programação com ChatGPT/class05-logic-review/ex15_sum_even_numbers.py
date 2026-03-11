total = 0
start = 1

while start <= 100:
    if start %2 == 0:
        total += start
    start += 1

print(f'Total Sum: {total}')