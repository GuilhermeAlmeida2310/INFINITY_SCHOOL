print('The first number need be bigger of the second number!')

number1 = int(input('Insert the first number: '))
number2 = int(input('Insert the second number: '))


if number1 <= number2:
    start = number1
    end = number2
else:
    start = number2
    end = number1

while start <= end:
    if start %2 == 0:
        print(start)
    start += 1
    