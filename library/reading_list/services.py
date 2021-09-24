from library.adapters.repository import AbstractRepository
from library.domain.model import Book, User


class NonExistentBookException(Exception):
    pass


def get_book_by_id(book_id: int, repo: AbstractRepository):
    book = repo.get_book_by_id(book_id)

    if book is None:
        raise NonExistentBookException

    return book


def get_page_of_books(cursor, books_per_page, repo: AbstractRepository, book_list=None):
    if book_list is None:
        books = repo.get_page_of_books(cursor, books_per_page)
    else:
        books = repo.get_page_of_books(cursor, books_per_page, book_list)
    return books


def get_user(user_name, repo: AbstractRepository):
    return repo.get_user(user_name)


def get_reading_list_length(user_name, repo: AbstractRepository):
    return repo.get_reading_list_length(user_name)


def read_a_book(book: Book, user: User, repo: AbstractRepository):
    repo.add_read_book(book, user)


def remove_read_book(book: Book, user: User, repo: AbstractRepository):
    repo.remove_read_book(book, user)


def get_reading_list(user_name, repo: AbstractRepository):
    return repo.get_reading_list(user_name)