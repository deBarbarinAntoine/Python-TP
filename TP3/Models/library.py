try:
    from TP3.Models.book import Book
except ImportError:
    from book import Book


class Library:
    """
    Class representing a book library.
    """

    def __init__(self, name: str):
        """
        Library constructor.
        :param name: the name of the library
        """
        self.name: str = name
        self.books: list[Book] = []

    @staticmethod
    def new(name: str) -> 'Library':
        """
        Static small factory method to create a new library.
        :param name: the name of the library
        :return: the created library
        """
        return Library(name)

    def add_book(self, book: Book) -> Book:
        """
        Adds a book to the library.
        :param book: the book to add
        :return: the added book
        """
        self.books.append(book)
        return book

    def add_book_by_isbn(self, isbn: str) -> tuple["Book", bool]:
        """
        Adds a book to the library by ISBN using Google Books API.
        :param isbn: the ISBN of the book
        :return: a tuple with the new book and a boolean indicating if the book was created or not.
        """
        book, ok = Book.new_by_isbn(isbn)
        if ok:
            self.books.append(book)
            return book, ok
        return book, False

    def remove_book(self, book: Book) -> bool:
        """
        Removes a book from the library.
        :param book: the book to remove.
        :return: the boolean indicating if the book was removed or not.
        """
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def remove_book_by_isbn(self, isbn: str) -> bool:
        """
        Removes a book from the library by ISBN.
        :param isbn: the ISBN of the book (empty ISBN returns False).
        :return: the boolean indicating if the book was removed or not.
        """
        isbn = isbn.strip()
        if isbn == "": return False
        for book in self.books:
            if book.get_isbn() == isbn:
                self.books.remove(book)
                return True
        return False

    def remove_book_by_id(self, book_id: int) -> bool:
        """
        Removes a book from the library by id.
        :param book_id: the id of the book to remove.
        :return: the boolean indicating if the book was removed or not.
        """
        for book in self.books:
            if book.get_id() == book_id:
                self.books.remove(book)
                return True
        return False

    def display_books(self, to_stdout: bool = False) -> str:
        """
        Displays the books in the library.
        :param to_stdout: whether to print the result in the stdout or not.
        :return: the string with all the books in the library
        """
        if to_stdout:
            print(self)
        return self.__str__()

    def __str__(self):
        buffer: str = ""
        for book in self.books:
            buffer += str(book) + "\n"
        return buffer