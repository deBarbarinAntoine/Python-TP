from datetime import datetime
import requests


class Book:
    """
    Class representing a book.
    """
    _id: int = 0
    """static value to set the unique identifier of the book."""
    __max_len_author: int = 70
    """static value to set the maximum length of the author of the book."""
    __max_len_title: int = 120
    """static value to set the maximum length of the title of the book."""
    __max_len_publisher: int = 70
    """static value to set the maximum length of the publisher of the book."""
    __min_publication_year: int = 1450
    """static value to set the minimum publication year of the book."""
    __isbn_lengths: list[int | tuple[int, int]] = [10, 13]
    """static list with valid ISBN lengths (int) of ranges of length (tuple[int, int])."""

    @staticmethod
    def check_isbn(isbn: str) -> bool:
        """
        Checks if an ISBN is valid.
        :param isbn: the ISBN to be checked
        :return: true if the ISBN is valid, false otherwise
        """
        for isbn_length in Book.__isbn_lengths:
            if type(isbn_length) == int and len(isbn) == isbn_length:
                return True
            elif type(isbn_length) == tuple[int, int]:
                min_, max_ = isbn_length
                if min_ > max_:
                    max_, min_ = min_, max_
                if min_ >= len(isbn) >= max_:
                    return True
        return False

    def _set_id(self):
        """
        Sets the unique identifier of the book according to the static attribute _id of the class.
        :return: None
        """
        Book._id += 1
        self._id = Book._id

    def get_id(self) -> int:
        """Gets the unique identifier of the book."""
        return self._id

    def __init__(self, title: str, authors: list[str], publication_year: int, publisher: str, isbn: str, id_: int = -1):
        """
        Constructs a new book.
        :param title: the title of the book.
        :param authors: the authors of the book.
        :param publication_year: the publication year of the book.
        :param publisher: the publisher of the book.
        :param isbn: the ISBN of the book.
        :param id_: the unique identifier of the book.
        """
        if id_ < 0:
            self._set_id()
        else:
            self._id = id_

        self._title: str = title
        self._isbn: str = isbn
        self._publication_year: int = publication_year
        self._publisher: str = publisher
        self._authors: list[str] = authors

    @staticmethod
    def new(title: str, *authors: str, publication_year: int = datetime.now().year, publisher: str = "",
            isbn: str = "") -> tuple["Book", bool]:
        """
        Static small factory to create a new book.
        :param title: the title of the book.
        :param authors: the authors of the book.
        :param publication_year: the publication year of the book.
        :param publisher: the publisher of the book.
        :param isbn: the ISBN of the book.
        :return: a tuple with the new book and a boolean indicating if the book was created or not.
        """
        valid_authors: list[str] = []

        for author in authors:
            author = author.strip().title()

            if 0 < len(author) <= Book.__max_len_author:
                valid_authors.append(author)

        if len(valid_authors) <= 0 \
                or 0 >= len(title) > Book.__max_len_title \
                or Book.__min_publication_year > publication_year > datetime.now().year \
                or 0 > len(publisher) > Book.__max_len_publisher \
                or (isbn != "" and not Book.check_isbn(isbn)):
            return Book.empty(), False

        return Book(title, valid_authors, publication_year, publisher, isbn), True

    @staticmethod
    def new_by_isbn(isbn: str) -> tuple["Book", bool]:
        """
        Static small factory to create a new book with the ISBN using Google Books API.
        :param isbn: the ISBN of the book.
        :return: a tuple with the new book and a boolean indicating if the book was created or not.
        """
        isbn = isbn.strip()
        isbn = isbn.replace("-", "")

        query = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(query)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return Book.empty(), False

        # DEBUG
        # print(response.json())

        response = response.json()

        if response["totalItems"] >= 1:
            return Book._from_json(response["items"][0]["volumeInfo"], isbn)

        return Book.empty(), False

    @staticmethod
    def _from_json(book_json, isbn_search) -> tuple["Book", bool]:
        """
        Creates a new book from the JSON response (coming from Google Books API).
        :param book_json: the JSON response from the Google Books API.
        :param isbn_search: the ISBN of the book.
        :return: a tuple with the new book and a boolean indicating if the book was created or not.
        """
        title: str = book_json["title"]
        authors: list[str] = book_json["authors"]
        publisher: str = ""

        try:
            publisher = book_json["publisher"]
        except KeyError:
            pass

        publication_year = int(book_json["publishedDate"])
        isbn: str = ""

        if len(book_json["industryIdentifiers"]) > 0:
            for industry_identifier in book_json["industryIdentifiers"]:
                if industry_identifier["type"] == "ISBN_13":
                    isbn = industry_identifier["identifier"]
                if isbn == "" and Book.check_isbn(industry_identifier["identifier"]):
                    isbn = industry_identifier["identifier"]

        if isbn == "" and Book.check_isbn(isbn_search):
            isbn = isbn_search

        # DEBUG
        # print(f"title: {title}")
        # print(f"authors: {authors}")
        # print(f"publisher: {publisher}")
        # print(f"publication_year: {publication_year}")
        # print(f"isbn: {isbn}")

        return Book.new(title, publication_year=publication_year, publisher=publisher, isbn=isbn, *authors)

    @staticmethod
    def empty() -> "Book":
        """Creates an empty book with id 0."""
        return Book("", [], 0, "", "", 0)

    def add_author(self, author: str) -> bool:
        """
        Adds an author to the book.
        :param author: the author to be added.
        :return: the boolean indicating if the author was added or not.
        """
        if author not in self._authors:
            if 0 < len(author) <= Book.__max_len_author:
                self._authors.append(author)
                return True
        return False

    def remove_author(self, author: str) -> bool:
        """
        Removes an author from the book.
        :param author: the author to be removed.
        """
        try:
            self._authors.remove(author)
            return True
        except ValueError:
            return False

    def get_authors(self) -> list[str]:
        """Gets the list of the authors of the book."""
        return self._authors

    def get_title(self) -> str:
        """Gets the title of the book."""
        return self._title

    def set_title(self, title: str) -> bool:
        """
        Sets the title of the book.
        :param title: the new title of the book.
        :return: the boolean indicating if the title of the book was updated or not.
        """
        if 0 < len(title) <= Book.__max_len_title:
            self._title = title
            return True
        return False

    def get_isbn(self) -> str:
        """Gets the ISBN of the book."""
        return self._isbn

    def set_isbn(self, isbn: str) -> bool:
        """
        Sets the ISBN of the book.
        :param isbn: the new ISBN of the book.
        :return: the boolean indicating if the ISBN of the book was updated or not.
        """
        if Book.check_isbn(isbn):
            self._isbn = isbn
            return True
        return False

    def get_publication_year(self) -> int:
        """Gets the publication year of the book."""
        return self._publication_year

    def set_publication_year(self, publication_year: int) -> bool:
        """
        Sets the publication year of the book.
        :param publication_year: the new publication year of the book.
        :return: the boolean indicating if the publication year of the book was updated or not.
        """
        if Book.__min_publication_year <= publication_year <= datetime.now().year:
            self._publication_year = publication_year
            return True
        return False

    def get_publisher(self) -> str:
        """Gets the publisher of the book."""
        return self._publisher

    def set_publisher(self, publisher: str) -> bool:
        """
        Sets the publisher of the book.
        :param publisher: the new publisher of the book.
        :return: the boolean indicating if the publisher of the book was updated or not.
        """
        if 0 <= len(publisher) <= Book.__max_len_publisher:
            self._publisher = publisher
            return True
        return False

    def __str__(self) -> str:
        return f"""
#########################################################
〰> Book nº{self._id}
---------------------------------------------------------
• Title: {self._title}
• Authors: {', '.join(self._authors)}
• Publication year: {self._publication_year}
• Publisher: {self._publisher}
• ISBN: {self._isbn}
#########################################################
"""

if __name__ == "__main__":
    book, ok = Book.new_by_isbn("978-0-0071-2381-0")
    if ok:
        print(book)

    book, ok = Book.new_by_isbn("978-0-5450-1022-1")
    if ok:
        print(book)

    book, ok = Book.new_by_isbn("978-3-8273-2824-3")
    if ok:
        print(book)

    book, ok = Book.new_by_isbn("978-1-5932-7828-1")
    if ok:
        print(book)
