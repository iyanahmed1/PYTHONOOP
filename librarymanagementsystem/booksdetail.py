class Book():
    def __init__(self,title,author,isbn,avaliable):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=avaliable
    #method string 
    def __str__(self):
        print(f"Title{self.title},Author{self.author},ISBN{self.isbn},Available:{'Yes' if self.available else 'No'}")

class Library():
    def __init__(self):
        self.books=[]
     # add a book 
    def add_book(self,book):
        self.books.extend(book)
     # remove books
    def remove_book(self,isbn):
        self.books=[ book for book in self.books if self.isbn != isbn ]
    # find books
    def find_books(self,isbn):
        for book in self.books:
            if book == isbn:
                return book
            return None
    def list_books(book):
        return[str(book)for book in book]
    
    


        