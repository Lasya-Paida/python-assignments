class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class DigitalBook(Book):
    def __init__(self, title, author, size_mb):
        super().__init__(title, author)
        self.size_mb = size_mb

    def __str__(self):
        return f"{super().__str__()} [Digital, {self.size_mb}MB]"

class AudioBook(Book):
    def __init__(self, title, author, duration_min):
        super().__init__(title, author)
        self.duration_min = duration_min

    def __str__(self):
        return f"{super().__str__()} [Audio, {self.duration_min} mins]"
