import pickle

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Checked Out'}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def list_books(self):
        print("Books in library:")
        for book in self.books:
            print(f" - {book}")

    def save_to_disk(self, filename="library.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        print(f"Library saved to {filename}")

    @staticmethod
    def load_from_disk(filename="library.pkl"):
        try:
            with open(filename, "rb") as f:
                library = pickle.load(f)
            print(f"Library loaded from {filename}")
            return library
        except FileNotFoundError:
            print("No saved library found. Creating new one.")
            return Library()