from library.adapters.repository import AbstractRepository
from library.domain.model import Book


class MemoryRepository(AbstractRepository):

    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__books = list()

    # testing
    def get_all_books(self):
        return self.__books

    def get_book_by_id(self, id: int):
        return next((book for book in self.__books if book.book_id == id), None)

    def add_book(self, book: Book):
        self.__books.append(book)

    def get_number_of_books(self):
        return len(self.__books)

    def get_page_of_books(self, cursor, books_per_page):
        if cursor * books_per_page + books_per_page >= len(self.__books):
            return self.__books[cursor * books_per_page:]
        else:
            return self.__books[cursor * books_per_page: cursor * books_per_page + books_per_page]


def populate(book_dataset, repo):
    for book in book_dataset:
        repo.add_book(book)
