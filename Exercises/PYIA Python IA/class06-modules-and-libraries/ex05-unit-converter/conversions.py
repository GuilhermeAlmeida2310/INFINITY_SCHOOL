import main

line = '-' * 30

def menu():
    while True:
        print('Unit Converter')
        print('1. Meters to Feets')
        print('2. Kilograms to Pounds')
        print('3. Celsius to Fahrenheit')
        print('4. Exit')

        option = int(input('Insert a number option: '))

        if option == 1:
            meters = float(input('Insert the amount of meters: '))
            result = main.converter_meters(meters)
            print(f'Conversion: {result:.2f}')
            print(line)

        elif option == 2:
            kilograms = float(input('Insert the amount of kilograms: '))
            result = main.converter_kilograms(kilograms)
            print(f'Conversion: {result:.2f}')
            print(line)

        elif option == 3:
            celsius = float(input('Insert the amount of celsius: '))
            result = main.converter_celsius(celsius)
            print(f'Conversion: {result:.2f}')
            print(line)

        elif option == 4:
            print('Exiting...')
            break

        else:
            print('Insert a valid option!')
            continue

menu()