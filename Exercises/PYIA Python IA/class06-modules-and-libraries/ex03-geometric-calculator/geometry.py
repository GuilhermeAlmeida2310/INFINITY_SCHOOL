import main
import math

line = '-' * 30

def menu():
    while True:
        print('Calculator of Simple Geometry Forms')
        print('1. Square')
        print('2. Rectangle')
        print('3. Circle')
        print('4. Exit')

        option = int(input('Insert a number option: '))

        if option == 1:
            length = float(input('Insert a length of square: '))

            if length < 0:
                print('Insert positive numbers!')
                print(line)
            else:
                perimeter = length * 4
                area = length * length
                result = main.calculate_square(f'{perimeter:.2f}', f'{area:.2f}')
                print(result)
                print(line)
    
        elif option == 2:
            base = float(input('Insert a base of rectangle: '))
            height = float(input('Insert a height of rectangle: '))

            if base < 0 or height < 0:
                print('Insert positive numbers!')
                print(line)
            else:
                perimeter = 2 * (base + height)
                area = base * height
                result = main.calculate_rectangle(f'{perimeter:.2f}', f'{area:.2f}')
                print(result)
                print(line)

        elif option == 3:
            radius = float(input('Insert the value of radius: '))

            if radius < 0:
                print('Insert positive numbers!')
                print(line)
            else:
                perimeter = 2 * math.pi * radius
                area = math.pi * (radius ** 2)
                result = main.calculate_circle(f'{perimeter:.2f}', f'{area:.2f}')
                print(result)
                print(line)

        elif option == 4:
            print('Exiting...')
            break

        else:
            print('Insert a valid option!')
            print(line)
            continue

menu()
