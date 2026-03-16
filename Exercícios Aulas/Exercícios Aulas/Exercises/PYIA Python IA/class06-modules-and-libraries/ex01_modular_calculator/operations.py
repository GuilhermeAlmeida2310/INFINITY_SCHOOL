import main

line = '-' * 30

def menu():
    while True:
        print('1. Add Numbers')
        print('2. Subtract Numbers')
        print('3. Multiply Numbers')
        print('4. Dividing Numbers')
        print('5. Exit')
        print('Choose the numbers for make the operation!')
        
        option = int(input('Insert a option: '))

        if option == 1:
            num1 = float(input('Insert the first number: '))
            num2 = float(input('Insert the second number: '))
            total_sum = main.number_sum(num1,num2)
            print(f'{num1} + {num2} = {total_sum}')
            print(line)

        elif option == 2:
            num1 = float(input('Insert the first number: '))
            num2 = float(input('Insert the second number: '))
            total_sub = main.number_sub(num1, num2)
            print(f'{num1} - {num2} = {total_sub}')
            print(line)

        elif option == 3:
            num1 = float(input('Insert the first number: '))
            num2 = float(input('Insert the second number: '))
            total_mult = main.number_mult(num1, num2)
            print(f'{num1} X {num2} = {total_mult}')
            print(line)

        elif option == 4:
            num1 = float(input('Insert the first number: '))
            num2 = float(input('Insert the second number: '))
            total_divi = main.number_divi(num1, num2)
            print(f'{num1} ÷ {num2} = {total_divi}')
            print(line)
            
        elif option == 5:
            print('Exiting...')
            break

        else:
            print('Insert a valid option please!')
            continue

menu()