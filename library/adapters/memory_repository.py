from library.adapters.repository import AbstractRepository, RepositoryException
from library.adapters.jsondatareader import BooksJSONReader
from library.domain.model import Book


class MemoryRepository(AbstractRepository):

    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__books = list()

    def get_book_by_id(self):
        return next((book for book in self.__books if book.book_id == id), None)

    def add_book(self, book: Book):
        self.__books.append(book)


def populate(book_dataset, repo):
    for book in book_dataset:
        repo.add_book(book)
