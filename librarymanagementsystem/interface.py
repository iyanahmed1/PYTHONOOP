from booksdetail import Book,  Library

#when you open the system
def main():
    library=Library()

    while True:
        print('Library Management System')
        print('1.Please add a new book.')
        print('2. please remove a book')
        print('3. Please find a book')
        print('4.List all the books')
        print('5. Exist')
        choice=input('Please enter your choice(1,2,3,4,5)')
        if choice=='1':
            title=input('Please enter the title: ')
            author=input('Please enter the author: ')
            isbn=input('Please enter the isbn: ')
            available=input('Please if the book is available? (yes or no)')
            book=Book(title,author,isbn,available)
            print('Book added')
        elif choice=='2':
            isbn=input('Please enter the isbn of the book to be removed: ')
            Library.remove_book(isbn)
            print('Book removed')
        elif choice=='3':
            isbn=('Please enter the isbn of the book to be found: ')
            book= Library.find_books(isbn)
            if book:
                print(book)
            else:
                print('The book is not found')
        elif choice=='4':
            books=Library.list_books()
            if books:
                for book in books:
                    print(book)
            else:
                print('No books available.')
        elif choice=='5':
            print('Exist')
            break
        else:
            print('Invalid choice.Try again')
if __name__ =='__main__':
    main()
    


# Open the file in write mode
file = open('interface.txt', 'w')
file.close()

#print("File 'interface.txt' has been created successfully.")



