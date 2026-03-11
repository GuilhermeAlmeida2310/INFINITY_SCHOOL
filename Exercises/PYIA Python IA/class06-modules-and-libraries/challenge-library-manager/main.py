import user
import library

line = '-' * 30

books = []
users = []
loans = {}

def menu():
    while True:
        print('1. User Registration')
        print('2. User Loan')
        print('3. Book Registration')
        print('4. List Books')
        print('5. Book Availability')
        print('6. View Loans')
        print('7. Exit')

        option = int(input('Insert a number option: '))

        if option == 1:
            name = input('Insert your name: ')
            age = int(input('Insert your age: '))
            phone = int(input('Insert your phone number: '))
            person = user.user_registration(name, age, phone)
            users.append(person)
            print(f'User registered: {person}')
            print(line)

        elif option == 2:
            name = input('Insert your name: ')

            user_found = None
            for i in users:
                if i[0] == name:
                    user_found = i
                    break
            
            if user_found is None:
                print('That name is not registered in the system!')
                print(line)
                continue

            title = input('Insert the book title: ')

            book_found = None
            book_position = -1
            for i in range(len(books)):
                if books[i][0] == title:
                    book_found = books[i]
                    book_position = i
                    break
            
            if book_found is None:
                print('That book is not registered in the system!')
                print(line)
                continue

            book_title, author, copies = book_found
            if copies <= 0:
                print('Book unavailable at the moment!')
                print(line)
                continue

            books[book_position] = (book_title, author, copies - 1)

            if name in loans:
                loans[name].append(title)
            else:
                loans[name] = [title]

            print(f'Book "{title}" loaned successfully to {name}!')
            print(line)

        elif option == 3:
            title = input('Insert the book title: ')
            author = input('Insert the author name: ')
            number_copies = int(input('Insert the number of copies: '))
            book = library.add_book(title, author, number_copies)
            books.append(book)
            print(f'Book registered: {book}')
            print('The book was registered successfully!')
            print(line)

        elif option == 4:
            print('List of Books:')
            for book in books:
                print(f'Title: {book[0]}, Author: {book[1]}, Copies: {book[2]}')
            print(line)

        elif option == 5:
            title = input('Insert the book title: ')

            book_found = None
            for book in books:
                if book[0] == title:
                    book_found = book
                    break

            if book_found is None:
                print('The book was not registered!')
                print(line)
                continue
            
            book_title, author, copies = book_found
            if copies <= 0:
                print('That book is unavailable at the moment!')
                print(f'Copies available: {copies}')
            else:
                print(f'Book "{book_title}" is available!')
                print(f'Copies available: {copies}')
            print(line)

        elif option == 6:
            print('--- LOANS ---')
            if loans:
                for user_name, books_list in loans.items():
                    print(f'User: {user_name}')
                    for book in books_list:
                        print(f'  - {book}')
            else:
                print('No loans registered.')
            print(line)

        elif option == 7:
            print('Exiting...')
            break

        else:
            print('Insert a valid option!')
            print(line)
            continue

menu()