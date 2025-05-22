import json
import os
from book import Book, DigitalBook, AudioBook
from user import User

DATA_FILE = os.path.join(os.path.dirname(__file__), "library.json")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        new_user = User(name)
        self.users.append(new_user)
        return new_user

    def borrow_book(self, username, book_title):
        user = self.find_user(username)
        for book in self.books:
            if book.title == book_title and book.available:
                book.available = False
                user.borrow_book(book)
                return f"{username} borrowed {book_title}"
        return f"{book_title} is not available"

    def return_book(self, username, book_title):
        user = self.find_user(username)
        for book in user.borrowed_books:
            if book.title == book_title:
                book.available = True
                user.return_book(book)
                return f"{username} returned {book_title}"
        return f"{book_title} was not borrowed by {username}"

    def list_books(self):
        return [
            f"{str(book)} {'(Available)' if book.available else '(Borrowed)'}"
            for book in self.books
        ]

    def save_data(self):
        data = {
            "books": [
                {
                    "type": book.__class__.__name__,
                    "title": book.title,
                    "author": book.author,
                    "available": book.available,
                    "size_mb": getattr(book, "size_mb", None),
                    "duration_min": getattr(book, "duration_min", None),
                }
                for book in self.books
            ]
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data.get("books", []):
                btype = item.get("type")
                if btype == "Book":
                    book = Book(item["title"], item["author"])
                elif btype == "DigitalBook":
                    book = DigitalBook(item["title"], item["author"], item["size_mb"])
                elif btype == "AudioBook":
                    book = AudioBook(item["title"], item["author"], item["duration_min"])
                else:
                    continue
                book.available = item.get("available", True)
                self.books.append(book)
