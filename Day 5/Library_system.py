class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book_title):
        book = library.lend_book(book_title)
        if book:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, library, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                library.receive_book(book)
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} does not have the book '{book_title}'.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return book
        print(f"Book '{title}' is not available.")
        return None

    def receive_book(self, book):
        book.available = True
        print(f"Book '{book.title}' returned to library.")

    def show_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f" - {book}")
        print()

library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

user1 = User("Alice")

library.show_available_books()

user1.borrow_book(library, "1984")
library.show_available_books()

user1.return_book(library, "1984")
library.show_available_books()