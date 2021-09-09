from typing import Iterable

from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher


class NonExistentBookException(Exception):
    pass


def get_book_by_id(book_id: int, repo: AbstractRepository):
    book = repo.get_book_by_id(book_id)

    if book is None:
        raise NonExistentBookException

    return book_to_dict(book)


def book_to_dict(books: Iterable[Book]):
    return [book_to_dict(book) for book in books]
