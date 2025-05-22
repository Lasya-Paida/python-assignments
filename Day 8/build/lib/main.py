import argparse
from book import Book, DigitalBook, AudioBook
from library import Library

def main():
    lib = Library()
    parser = argparse.ArgumentParser(description="Library System CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add book
    add_parser = subparsers.add_parser("add_book")
    add_parser.add_argument("type", choices=["book", "digital", "audio"])
    add_parser.add_argument("title")
    add_parser.add_argument("author")
    add_parser.add_argument("--size", type=float, help="Size in MB for digital books")
    add_parser.add_argument("--duration", type=int, help="Duration in minutes for audio books")

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
            book = DigitalBook(args.title, args.author, args.size)
        elif args.type == "audio":
            book = AudioBook(args.title, args.author, args.duration)
        lib.add_book(book)
        lib.save_data()
        print(f"{args.type.capitalize()} added: {book}")

    elif args.command == "list_books":
        books = lib.list_books()
        if not books:
            print("No books available.")
        else:
            for b in books:
                print(b)

    elif args.command == "borrow":
        result = lib.borrow_book(args.user, args.title)
        print(result)
        lib.save_data()

    elif args.command == "return":
        result = lib.return_book(args.user, args.title)
        print(result)
        lib.save_data()

if __name__ == "__main__":
    main()
