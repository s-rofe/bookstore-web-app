from typing import Iterable

from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher


class NonExistentBookException(Exception):
    pass


def get_book_by_id(book_id: int, repo: AbstractRepository):
    book = repo.get_book_by_id(book_id)

    if book is None:
        raise NonExistentBookException

    return book


def get_all_books(repo: AbstractRepository):
    return repo.get_all_books()


def get_page_of_books(cursor, books_per_page, repo: AbstractRepository):
    books = repo.get_page_of_books(cursor, books_per_page)
    return books


def get_number_of_books(repo: AbstractRepository):
    return repo.get_number_of_books()

