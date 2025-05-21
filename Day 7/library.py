import json

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {"type": "Book", "title": self.title, "author": self.author, "available": self.available}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data.get("available", True))

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"

class DigitalBook(Book):
    def __init__(self, title, author, file_size_mb, available=True):
        super().__init__(title, author, available)
        self.file_size_mb = file_size_mb

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "DigitalBook"
        d["file_size_mb"] = self.file_size_mb
        return d

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["file_size_mb"], data.get("available", True))

    def __str__(self):
        return super().__str__() + f" [DigitalBook, {self.file_size_mb}MB]"

class AudioBook(Book):
    def __init__(self, title, author, duration_minutes, available=True):
        super().__init__(title, author, available)
        self.duration_minutes = duration_minutes

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "AudioBook"
        d["duration_minutes"] = self.duration_minutes
        return d

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["duration_minutes"], data.get("available", True))

    def __str__(self):
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60
        duration_str = f"{hours}h {minutes}m" if hours else f"{minutes}m"
        return super().__str__() + f" [AudioBook, Duration: {duration_str}]"

class User:
    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books or []

    def to_dict(self):
        return {"name": self.name, "borrowed_books": self.borrowed_books}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("borrowed_books", []))

    def __str__(self):
        books = ', '.join(self.borrowed_books) or "No books borrowed"
        return f"User: {self.name}, Borrowed books: {books}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def lend_book(self, title, user_name):
        book = self.find_book(title)
        if not book:
            print(f"Book '{title}' not found.")
            return False
        if not book.available:
            print(f"Book '{title}' is not available.")
            return False
        user = self.find_user(user_name)
        if not user:
            user = User(user_name)
            self.users.append(user)
        book.available = False
        user.borrowed_books.append(book.title)
        print(f"'{title}' lent to {user_name}.")
        return True

    def receive_book(self, title, user_name):
        book = self.find_book(title)
        if not book:
            print(f"Book '{title}' not found.")
            return False
        user = self.find_user(user_name)
        if not user or title not in user.borrowed_books:
            print(f"{user_name} did not borrow '{title}'.")
            return False
        book.available = True
        user.borrowed_books.remove(title)
        print(f"'{title}' returned by {user_name}.")
        return True

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def list_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f" - {book}")
        print()

    def save(self, filename="library_data.json"):
        data = {
            "books": [book.to_dict() for book in self.books],
            "users": [user.to_dict() for user in self.users]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")

    def load(self, filename="library_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.books = []
            for b in data.get("books", []):
                t = b.get("type", "Book")
                if t == "DigitalBook":
                    self.books.append(DigitalBook.from_dict(b))
                elif t == "AudioBook":
                    self.books.append(AudioBook.from_dict(b))
                else:
                    self.books.append(Book.from_dict(b))
            self.users = [User.from_dict(u) for u in data.get("users", [])]
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"No data file found ({filename}). Starting with empty library.")


import argparse

def main():
    library = Library()
    library.load()

    parser = argparse.ArgumentParser(description="Library CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add book command
    add_parser = subparsers.add_parser("add_book")
    add_parser.add_argument("type", choices=["book", "digital", "audio"])
    add_parser.add_argument("title")
    add_parser.add_argument("author")
    add_parser.add_argument("--size", type=float, help="File size in MB for digital books")
    add_parser.add_argument("--duration", type=int, help="Duration in minutes for audiobooks")

    # List books
    subparsers.add_parser("list_books")

    # Borrow book
    borrow_parser = subparsers.add_parser("borrow")
    borrow_parser.add_argument("user")
    borrow_parser.add_argument("title")

    # Return book
    return_parser = subparsers.add_parser("return")
    return_parser.add_argument("user")
    return_parser.add_argument("title")

    args = parser.parse_args()

    if args.command == "add_book":
        if args.type == "book":
            book = Book(args.title, args.author)
        elif args.type == "digital":
            if args.size is None:
                print("Error: --size is required for digital books")
                return
            book = DigitalBook(args.title, args.author, args.size)
        else:  # audio
            if args.duration is None:
                print("Error: --duration is required for audiobooks")
                return
            book = AudioBook(args.title, args.author, args.duration)
        library.add_book(book)

    elif args.command == "list_books":
        library.list_available_books()

    elif args.command == "borrow":
        library.lend_book(args.title, args.user)

    elif args.command == "return":
        library.receive_book(args.title, args.user)

    else:
        parser.print_help()

    library.save()

if __name__ == "__main__":
    main()
