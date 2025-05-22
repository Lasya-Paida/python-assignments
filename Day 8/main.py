import argparse
from book import Book, DigitalBook, AudioBook
from library import Library

lib = Library()

parser = argparse.ArgumentParser(description="Library System CLI")
subparsers = parser.add_subparsers(dest="command")

# Add book
add_parser = subparsers.add_parser("add_book")
add_parser.add_argument("type", choices=["book", "digital", "audio"])
add_parser.add_argument("title")
add_parser.add_argument("author")
add_parser.add_argument("--size", type=float)
add_parser.add_argument("--duration", type=int)

# List books
subparsers.add_parser("list_books")

# Borrow
borrow_parser = subparsers.add_parser("borrow")
borrow_parser.add_argument("user")
borrow_parser.add_argument("title")

# Return
return_parser = subparsers.add_parser("return")
return_parser.add_argument("user")
return_parser.add_argument("title")

args = parser.parse_args()

if args.command == "add_book":
    if args.type == "book":
        book = Book(args.title, args.author)
    elif args.type == "digital":
        book = DigitalBook(args.title, args.author, args.size)
    elif args.type == "audio":
        book = AudioBook(args.title, args.author, args.duration)
    lib.add_book(book)
    lib.save_data()
    print(f"{args.type.capitalize()} added: {book}")

elif args.command == "list_books":
    for b in lib.list_books():
        print(b)

elif args.command == "borrow":
    print(lib.borrow_book(args.user, args.title))
    lib.save_data()

elif args.command == "return":
    print(lib.return_book(args.user, args.title))
    lib.save_data()
