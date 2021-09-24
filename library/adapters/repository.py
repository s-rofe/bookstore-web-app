import abc
from library.domain.model import Publisher, Book, Author, User, Review

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
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews(self, book_id):
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
    def get_page_of_books(self, cursor, books_per_page, book_list=None):
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

    @abc.abstractmethod
    def get_books_by_title(self, title):
        raise NotImplementedError

    @abc.abstractmethod
    def increase_review_count(self, book_id, count):
        raise NotImplementedError

    @abc.abstractmethod
    def get_review_count(self, book_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reading_list_length(self, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review_to_user(self, review, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def add_read_book(self, book: Book, user: User):
        raise NotImplementedError

    def remove_read_book(self, book: Book, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reading_list(self, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def set_stored_url(self, url):
        return NotImplementedError

    @abc.abstractmethod
    def get_stored_url(self):
        return NotImplementedError
