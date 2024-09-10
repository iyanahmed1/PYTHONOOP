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
    
# Define the content for the text file
interface_content = """
Library Management System - User Interface Guide

1. Adding a New Book:
----------------------
   - Prompt: "Please enter the title: "
   - Prompt: "Please enter the author: "
   - Prompt: "Please enter the ISBN: "
   - Prompt: "Is the book available? (yes or no)"
   - Action: Creates a new Book object with the provided details and adds it to the library.

2. Removing a Book:
---------------------
   - Prompt: "Please enter the ISBN of the book to be removed: "
   - Action: Removes the book with the specified ISBN from the library.

3. Finding a Book:
--------------------
   - Prompt: "Please enter the ISBN of the book to be found: "
   - Action: Searches for the book with the specified ISBN in the library. If found, prints the book details; otherwise, informs the user that the book is not found.

4. Listing All Books:
-----------------------
   - Action: Lists all the books currently in the library. If there are no books, informs the user that no books are available.

5. Exiting the System:
------------------------
   - Action: Ends the interface and exits the program.

Instructions:
-------------
1. When the system starts, the user is presented with a menu with options to add, remove, find, list books, or exit.
2. Based on the user's choice, appropriate prompts are displayed to gather information or perform actions.
3. The system continuously loops until the user chooses to exit by selecting option '5'.

User Choices:
--------------
1. Add a new book
2. Remove a book
3. Find a book
4. List all books
5. Exit
"""

# Open the file in write mode
file = open('interface.txt', 'w')

# Write the content to the file
file.write(interface_content)

# Close the file to ensure all data is written and resources are freed
file.close()

print("File 'interface.txt' has been created successfully.")



