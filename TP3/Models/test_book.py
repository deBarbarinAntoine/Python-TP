import json
import unittest
from datetime import datetime
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

try:
    from TP3.Models.book import Book
except ImportError:
    from book import Book


class TestBook(TestCase):

    def test_check_isbn(self):
        self.assertTrue(Book.check_isbn("9780007123810"))
        self.assertTrue(Book.check_isbn("9780007123"))

        self.assertFalse(Book.check_isbn("97800071238101"))
        self.assertFalse(Book.check_isbn("97800071238"))

    def test_get_id(self):
        empty_book = Book.empty()
        self.assertEqual(empty_book.get_id(), 0)

        book, ok = Book.new("test", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertEqual(book.get_id(), Book._id)

    def test_new(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)

    def test_new_by_isbn(self):
        book, ok = Book.new_by_isbn("978-1-5932-7828-1")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_title(), "The Rust Programming Language")
        self.assertEqual(book.get_authors(), ["Steve Klabnik", "Carol Nichols"])

    def test__from_json(self):
        json_str = """
      {
        "title": "Design Patterns",
        "subtitle": "Elements of Reusable Object-Oriented Software",
        "authors": [
          "Erich Gamma",
          "Richard Helm",
          "Ralph Johnson",
          "John Vlissides"
        ],
        "publisher": "Pearson Deutschland GmbH",
        "publishedDate": "1995",
        "description": "Software -- Software Engineering.",
        "industryIdentifiers": [
          {
            "type": "ISBN_10",
            "identifier": "3827328241"
          },
          {
            "type": "ISBN_13",
            "identifier": "9783827328243"
          }
        ],
        "readingModes": {
          "text": false,
          "image": true
        },
        "pageCount": 512,
        "printType": "BOOK",
        "categories": [
          "Business & Economics"
        ],
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "0.3.5.0.preview.1",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=jUvf7wMUGcUC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=jUvf7wMUGcUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.fr/books?id=jUvf7wMUGcUC&printsec=frontcover&dq=isbn:9783827328243&hl=&cd=1&source=gbs_api",
        "infoLink": "http://books.google.fr/books?id=jUvf7wMUGcUC&dq=isbn:9783827328243&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Design_Patterns.html?hl=&id=jUvf7wMUGcUC"
      }
"""
        json_book = json.loads(json_str)
        book, ok = Book._from_json(json_book, "9783827328243")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_title(), "Design Patterns")
        self.assertEqual(book.get_authors(), ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"])

    def test_empty(self):
        empty_book = Book.empty()
        self.assertIsNotNone(empty_book)
        self.assertIsInstance(empty_book, Book)
        self.assertEqual(empty_book.get_id(), 0)
        self.assertEqual(empty_book.get_publication_year(), 0)
        self.assertEqual(empty_book.get_title(), "")
        self.assertEqual(empty_book.get_authors(), [])

    def test_add_author(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_authors(), ["Test"])

        ok = book.add_author("Duck")
        self.assertTrue(ok, "error adding author.")
        self.assertEqual(book.get_authors(), ["Test", "Duck"])

    def test_remove_author(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_authors(), ["Test"])

        ok = book.remove_author("Duck")
        self.assertFalse(ok, "error removing author.")
        self.assertEqual(book.get_authors(), ["Test"])

        ok = book.remove_author("Test")
        self.assertTrue(ok, "error removing author.")
        self.assertEqual(book.get_authors(), [])

    def test_get_authors(self):
        book, ok = Book.new("testing", "Test", "Duck", "John Doe", "John R. R. Tolkien")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_authors(), ["Test", "Duck", "John Doe", "John R. R. Tolkien"])

    def test_get_title(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_title(), "testing")

    def test_set_title(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_title(), "testing")

        ok = book.set_title("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin aliquet purus at metus ultrices, sagittis hendrerit orci.")
        self.assertTrue(ok, "error setting max-length title.")
        self.assertEqual(book.get_title(), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin aliquet purus at metus ultrices, sagittis hendrerit orci.")

        ok = book.set_title("My book")
        self.assertTrue(ok, "error setting normal title.")
        self.assertEqual(book.get_title(), "My book")

        ok = book.set_title("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel metus mauris. Sed hendrerit aliquam turpis id dui.")
        self.assertFalse(ok, "error setting overflowing title.")
        self.assertEqual(book.get_title(), "My book")

        ok = book.set_title("")
        self.assertFalse(ok, "error setting empty title.")
        self.assertEqual(book.get_title(), "My book")

    def test_get_isbn(self):
        book1, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book1)
        self.assertIsInstance(book1, Book)
        self.assertEqual(book1.get_isbn(), "")

        book2, ok = Book.new("testing", "Test", isbn = "9783827328243")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book2)
        self.assertIsInstance(book2, Book)
        self.assertEqual(book2.get_isbn(), "9783827328243")

    def test_set_isbn(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_isbn(), "")

        ok = book.set_isbn("9783827328243")
        self.assertTrue(ok, "error setting good ISBN.")
        self.assertEqual(book.get_isbn(), "9783827328243")

        ok = book.set_isbn("978382732824")
        self.assertFalse(ok, "error setting bad ISBN.")
        self.assertEqual(book.get_isbn(), "9783827328243")

    def test_get_publication_year(self):
        book1, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book1)
        self.assertIsInstance(book1, Book)
        self.assertEqual(book1.get_publication_year(), datetime.now().year)

        book2, ok = Book.new("testing", "Test", publication_year = 1990)
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book2)
        self.assertIsInstance(book2, Book)
        self.assertEqual(book2.get_publication_year(), 1990)

    def test_set_publication_year(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_publication_year(), datetime.now().year)

        ok = book.set_publication_year(1990)
        self.assertTrue(ok, "error setting good publication year.")
        self.assertEqual(book.get_publication_year(), 1990)

        ok = book.set_publication_year(2030)
        self.assertFalse(ok, "error setting bad publication year.")
        self.assertEqual(book.get_publication_year(), 1990)

    def test_get_publisher(self):
        book1, ok = Book.new("testing", "Test", publisher = "PLON")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book1)
        self.assertIsInstance(book1, Book)
        self.assertEqual(book1.get_publisher(), "PLON")

        book2, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book2)
        self.assertIsInstance(book2, Book)
        self.assertEqual(book2.get_publisher(), "")

    def test_set_publisher(self):
        book, ok = Book.new("testing", "Test")
        self.assertTrue(ok, "error creating book.")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_publisher(), "")

        ok = book.set_publisher("Lorem ipsum dolor sit amet, consectetur adipiscing elit viverra fusce.")
        self.assertTrue(ok, "error setting max-length publisher.")
        self.assertEqual(book.get_publisher(), "Lorem ipsum dolor sit amet, consectetur adipiscing elit viverra fusce.")

        ok = book.set_publisher("PLON")
        self.assertTrue(ok, "error setting normal publisher.")
        self.assertEqual(book.get_publisher(), "PLON")

        ok = book.set_publisher("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at mi.")
        self.assertFalse(ok, "error setting bad publication year.")
        self.assertEqual(book.get_publisher(), "PLON")

def main() -> str:
    with patch('sys.stdout', new = StringIO()) as fake_out:
        unittest.main(verbosity=2)
        return fake_out.getvalue()

if __name__ == '__main__':
    print(main())