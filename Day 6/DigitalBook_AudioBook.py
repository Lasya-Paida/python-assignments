class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, available={self.available})"


class DigitalBook(Book):
    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
        self.file_size_mb = file_size_mb  # size in megabytes

    def __str__(self):
        base = super().__str__()
        return f"{base} [DigitalBook, {self.file_size_mb}MB]"

    def __repr__(self):
        return (f"DigitalBook(title={self.title!r}, author={self.author!r}, "
                f"file_size_mb={self.file_size_mb}, available={self.available})")


class AudioBook(Book):
    def __init__(self, title, author, duration_minutes):
        super().__init__(title, author)
        self.duration_minutes = duration_minutes  # length in minutes

    def __str__(self):
        base = super().__str__()
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60
        duration_str = f"{hours}h {minutes}m" if hours else f"{minutes}m"
        return f"{base} [AudioBook, Duration: {duration_str}]"

    def __repr__(self):
        return (f"AudioBook(title={self.title!r}, author={self.author!r}, "
                f"duration_minutes={self.duration_minutes}, available={self.available})")

ebook = DigitalBook("Digital Fortress", "Dan Brown", 2.5)
audiobook = AudioBook("Becoming", "Michelle Obama", 1140)  # 19 hours

print(ebook)
print(audiobook)
