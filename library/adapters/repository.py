import abc
from typing import List
from library.domain.model import Publisher, Book, Author, User, Review, BooksInventory

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_book(self, book: Book):
        raise NotImplementedError

    @abc.abstractmethod
    def add_author(self, author: Author):
        raise NotImplementedError

    @abc.abstractmethod
    def add_publisher(self, publisher: Publisher):
        raise NotImplementedError

    @abc.abstractmethod
    def add_release_year(self, release_year):
        raise NotImplementedError

    @abc.abstractmethod
    def get_authors(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_publishers(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_release_years(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_books(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_book_by_id(self, id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_books(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_page_of_books(self, cursor, books_per_page):
        raise NotImplementedError

    @abc.abstractmethod
    def get_books_with_author(self, author):
        raise NotImplementedError

    @abc.abstractmethod
    def get_books_with_publisher(self, publisher):
        raise NotImplementedError

    @abc.abstractmethod
    def get_books_with_release_year(self, release_year):
        raise NotImplementedError
