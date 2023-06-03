class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def borrow_book(self, book_id):
        book = self.search_book(book_id)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"You have borrowed {book.title}.")
            else:
                print("The book is currently unavailable.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.search_book(book_id)
        if book:
            if not book.is_available:
                book.is_available = True
                print(f"You have returned {book.title}.")
            else:
                print("This book is already in the library.")
        else:
            print("Book not found.")


library = Library()


book1 = Book("Python Programming", "John Smith", 101)
book2 = Book("Data Science Essentials", "Jane Doe", 102)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 103)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print("Books in the library:")
library.display_books()


print("\nBorrowing a book:")
library.borrow_book(102)

print("\nBooks in the library:")
library.display_books()


print("\nReturning a book:")
library.return_book(102)


print("\nBooks in the library:")
library.display_books()
