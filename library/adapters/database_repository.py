from sqlalchemy import desc, asc
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from library.domain.model import User, Book, Publisher, Review, Author
from library.adapters.repository import AbstractRepository


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_book(self, book: Book):
        pass

    def add_author(self, author: Author):
        pass

    def add_publisher(self, publisher: Publisher):
        pass

    def add_release_year(self, release_year):
        pass

    def get_authors(self):
        pass

    def get_publishers(self):
        pass

    def get_release_years(self):
        pass

    def add_user(self, user: User):
        pass

    def get_user(self, user_name):
        pass

    def add_review(self, review: Review):
        pass

    def get_reviews(self, book_id):
        pass

    def get_all_books(self):
        pass

    def get_book_by_id(self, id: int):
        pass

    def get_number_of_books(self):
        pass

    def get_page_of_books(self, cursor, books_per_page, book_list=None):
        pass

    def get_books_with_author(self, author):
        pass

    def get_books_with_publisher(self, publisher):
        pass

    def get_books_with_release_year(self, release_year):
        pass

    def get_books_by_title(self, title):
        pass

    def increase_review_count(self, book_id, count):
        pass

    def get_review_count(self, book_id):
        pass

    def get_reading_list_length(self, user_name):
        pass

    def add_review_to_user(self, review, user_name):
        pass

    def add_read_book(self, book: Book, user: User):
        pass

    def remove_read_book(self, book: Book, user: User):
        pass

    def get_reading_list(self, user_name):
        pass

    def set_stored_url(self, url):
        pass

    def get_stored_url(self):
        pass
