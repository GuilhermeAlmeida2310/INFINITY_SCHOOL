import main

line = '-' * 30

def menu():
    while True:
        print('String Operation')
        print('1. Invert Text')
        print('2. Counting Words')
        print('3. Verify Palindrome')
        print('4. Exit')
        print(line)

        option = int(input('Insert a option: '))

        if option == 1:
            text = input('Insert any text here: ')
            operation = main.invert_text(text)
            print(f'Inverted Word: {operation}')
            print(line)

        elif option == 2:
            text = input('Insert any text here: ')
            operation = main.counting_words(text)
            print(f'Number of Word: {operation}')
            print(line)

        elif option == 3:
            text = input('Insert any text here: ')

            start = 0
            end = len(text) - 1
            is_palindrome = True

            while start < end:
                if text[start] != text[end]:
                    is_palindrome = False
                    break
                start += 1
                end -= 1
                


            if is_palindrome:
                print('The word is a palindrome!')
                print(text)
                print(line)
            else:
                print('The word is not a palindrome!')
                print(line)

        elif option == 4:
            print('Exiting...')
            break

        else:
            print('Insert a valid option!')
            continue

menu()