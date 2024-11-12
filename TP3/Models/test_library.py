import unittest
from io import StringIO
from unittest import TestCase, TestLoader, TextTestRunner
from unittest.mock import patch

try:
    from TP3.Models.book import Book
    from TP3.Models.library import Library
except ImportError:
    from book import Book
    from library import Library


class TestLibrary(TestCase):
    def test_new(self):
        library = Library.new("Test")
        self.assertIsNotNone(library)
        self.assertIsInstance(library, Library)
        self.assertEqual(library.name, "Test")
        self.assertEqual(library.books, [])

    def test_add_book(self):
        library = Library.new("Testing")
        self.assertIsNotNone(library)
        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

        book1, ok = Book.new("My testing book", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book1)
        added_book = library.add_book(book1)
        self.assertEqual(added_book, book1)
        self.assertEqual(library.books, [book1])

        book2, ok = Book.new("My book test", "John Doe")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book2)
        added_book = library.add_book(book2)
        self.assertEqual(added_book, book2)
        self.assertEqual(library.books, [book1, book2])

    def test_add_book_by_isbn(self):
        library = Library.new("Test library")
        self.assertIsNotNone(library)
        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

        book1, ok = library.add_book_by_isbn("9781593278281")
        self.assertTrue(ok, "error adding book.")
        self.assertEqual(book1.get_title(), library.books[0].get_title())
        self.assertEqual(library.books, [book1])

        book2, ok = library.add_book_by_isbn("9783827328243")
        self.assertTrue(ok, "error adding book.")
        self.assertEqual(book2.get_title(), library.books[1].get_title())
        self.assertEqual(library.books, [book1, book2])

    def test_remove_book(self):
        library = Library.new("My library test")
        self.assertIsNotNone(library)
        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        library.add_book(book)
        self.assertEqual(library.books, [book])

        ok = library.remove_book(book)
        self.assertTrue(ok, "error removing book.")
        self.assertEqual(library.books, [])

        ok = library.remove_book(book)
        self.assertFalse(ok, "error removing book from empty library.")
        self.assertEqual(library.books, [])

    def test_remove_book_by_isbn(self):
        library = Library.new("My library")
        self.assertIsNotNone(library)
        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

        book1, ok = Book.new("Book of unit test", "John Doe")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book1)
        library.add_book(book1)
        self.assertEqual(library.books, [book1])

        book2, ok = Book.new("testing book", "Test", isbn = "9781593278281")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book2)
        library.add_book(book2)
        self.assertEqual(library.books, [book1, book2])

        ok = library.remove_book_by_isbn("")
        self.assertFalse(ok, "error removing book by blank ISBN")
        self.assertEqual(library.books, [book1, book2])

        ok = library.remove_book_by_isbn("9781593278281")
        self.assertTrue(ok, "error removing book by ISBN")
        self.assertEqual(library.books, [book1])

    def test_remove_book_by_id(self):
        library = Library.new("Public library")
        self.assertIsNotNone(library)
        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

        book, ok = Book.new("Unit test book", "Michael Foster")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        library.add_book(book)
        self.assertEqual(library.books, [book])

        ok = library.remove_book_by_id(0)
        self.assertFalse(ok, "error removing nonexistent book by id")
        self.assertEqual(library.books, [book])

        ok = library.remove_book_by_id(book.get_id())
        self.assertTrue(ok, "error removing book by id")
        self.assertEqual(library.books, [])

def test_library_run() -> str:
    test = TestLoader().loadTestsFromTestCase(TestLibrary)
    with patch('sys.stdout', new_callable = StringIO) as fake_out:
        TextTestRunner(stream=fake_out, verbosity=2).run(test)
        result = fake_out.getvalue()
        return result

if __name__ == '__main__':
    print(test_library_run())