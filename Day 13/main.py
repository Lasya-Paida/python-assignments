from library import Book, Library

library = Library.load_from_disk("Day 13/library.pkl")

library.add_book(Book("The Alchemist", "Paulo Coelho"))
library.add_book(Book("1984", "George Orwell", available=False))

library.list_books()

library.save_to_disk("Day 13/library.pkl")
