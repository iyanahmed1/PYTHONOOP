class Book():
    def __init__(self,title, author,isbn,avaliable=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=avaliable
    def __str__(self):
        return(f"Title{self.title}, Author{self.author}, ISBN{self.isbn}, Available:{'Yes'if  self.available else'No'}")

class Library():
    def __init__(self):
        self.books=[]
    #add a book
    def add_book(self,book):
        self.books.extend(book)
    #remove a book by isbn
    def remove_book(self,isbn):
        self.books=[ book for book in self.books if book.isbn != isbn]
        
    def find_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None    
    def list_book(book):
        return
#simple interface
def main():
    while True:
        print('Library Managment System')
        print('1. Please add a new book: ')
        print('2. Please remove a book: ')
        print('3. Please find a book: ')
        print('4. Please List all books.')
        choice=input('please enter your choice (1,2,3,4)')
        if choice=='1':
            title=input('please enter your title: ')
            author=input('please enter the author: ')
            isbn=input('Please enter the isbn: ')
            book=book(title,author,isbn)
            print('Book added')
            



