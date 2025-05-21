class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def get_description(self):
        return f"'{self.title}' by {self.author}"

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"{self.get_description()} - {status}"


class DigitalBook(Book):
    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
        self.file_size_mb = file_size_mb

    def get_description(self):
        return f"{super().get_description()} [DigitalBook, {self.file_size_mb}MB]"


class AudioBook(Book):
    def __init__(self, title, author, duration_minutes):
        super().__init__(title, author)
        self.duration_minutes = duration_minutes

    def get_description(self):
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60
        duration_str = f"{hours}h {minutes}m" if hours else f"{minutes}m"
        return f"{super().get_description()} [AudioBook, Duration: {duration_str}]"


books = [
    Book("Regular Book", "Author A"),
    DigitalBook("Digital Fortress", "Dan Brown", 2.5),
    AudioBook("Becoming", "Michelle Obama", 1140)
]

for book in books:
    print(book)          
    print(book.get_description())  
    print("---")
