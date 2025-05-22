import unittest
from library import Book, DigitalBook, AudioBook, User, Library

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Test Book", "Author A")
        self.digital = DigitalBook("Digital Book", "Author B", 10.5)
        self.audio = AudioBook("Audio Book", "Author C", 120)
        self.user_name = "Alice"

        self.library.add_book(self.book)
        self.library.add_book(self.digital)
        self.library.add_book(self.audio)

    def tearDown(self):
        # Clean up if needed
        self.library = None

    def test_add_and_find_book(self):
        found = self.library.find_book("Test Book")
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Test Book")

    def test_lend_and_receive_book(self):
        self.assertTrue(self.library.lend_book("Test Book", self.user_name))
        self.assertFalse(self.book.available)

        self.assertTrue(self.library.receive_book("Test Book", self.user_name))
        self.assertTrue(self.book.available)

    def test_borrow_unavailable_book(self):
        self.library.lend_book("Test Book", self.user_name)
        result = self.library.lend_book("Test Book", "Bob")
        self.assertFalse(result)

    def test_borrow_nonexistent_book(self):
        result = self.library.lend_book("Unknown Book", "Charlie")
        self.assertFalse(result)

    def test_return_unborrowed_book(self):
        result = self.library.receive_book("Digital Book", self.user_name)
        self.assertFalse(result)

    def test_user_creation_and_borrowing(self):
        self.library.lend_book("Audio Book", "Dave")
        user = self.library.find_user("Dave")
        self.assertIn("Audio Book", user.borrowed_books)

if __name__ == '__main__':
    unittest.main()
