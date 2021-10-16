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
        with self._session_cm as scm:
            scm.session.add(book)
            scm.commit()

    def add_author(self, author: Author):
        with self._session_cm as scm:
            scm.session.add(author)
            scm.commit()

    def add_publisher(self, publisher: Publisher):
        with self._session_cm as scm:
            scm.session.add(publisher)
            scm.commit()

    def add_release_year(self, release_year):
        # we dont use a release_year list in this repo
        # could use database_mode to make it only for the memory repo, or just pass if that works
        pass

    def get_authors(self):
        authors = self._session_cm.session.query(Author).all()
        return authors

    def get_publishers(self):
        publishers = self._session_cm.session.query(Publisher).all()
        return publishers

    def get_release_years(self):
        release_years = self._session_cm.session.query(Book.book_id).all()
        return release_years

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, new_user_name):
        user = self._session_cm.session.query(User.user_name).filter(User.user_name == new_user_name).one()
        return user

    def add_review(self, review: Review):
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()

    def get_reviews(self, book_id):
        reviews = self._session_cm.session.query(Review.book).filter(Book.book_id == book_id).all()
        return reviews

    def get_all_books(self):
        books = self._session_cm.session.query(Book).all()
        return books

    def get_book_by_id(self, id: int):
        book = self._session_cm.session.query(Book).filter(Book.book_id == id).one()
        return book

    def get_number_of_books(self):
        books = self._session_cm.session.query(Book).all()
        return len(books)

    def get_page_of_books(self, cursor, books_per_page, book_list=None):
        if book_list is None:
            book_list = self._session_cm.session.query(Book).all()
        if cursor * books_per_page + books_per_page >= self.get_number_of_books():
            return book_list[cursor * books_per_page:]
        else:
            return book_list[cursor * books_per_page: cursor * books_per_page + books_per_page]

    def get_books_with_author(self, author_name):
        author_name = author_name.lower()
        book_list = []
        all_books = self.get_all_books()
        for book in all_books:
            for author in book.authors:
                author_db_name = author.full_name.lower()
                if author_name in author_db_name:
                    book_list.append(book)
        return book_list

    def get_books_with_publisher(self, publisher_name):
        book_list = []
        publisher_name = publisher_name.lower()
        all_books = self.get_all_books()
        for book in all_books:
            pub_name = book.publisher.name.lower()
            if publisher_name in pub_name:
                book_list.append(book)
        return book_list

    def get_books_with_release_year(self, release_year):
        book_list = self._session_cm.session.query(Book).filter(Book.release_year == release_year).all()
        return book_list

    def get_books_by_title(self, title):
        book_list = []
        title = title.lower()
        all_books = self.get_all_books()
        for book in all_books:
            book_title = book.title.lower()
            if title in book_title:
                book_list.append(book)
        return book_list

    def increase_review_count(self, book_id, count):
        book = self._session_cm.session.query(Book).filter(Book.book_id == book_id).one()
        book.increase_total_ratings(count)

    def get_review_count(self, book_id):
        reviews = self._session_cm.session.query(book_id).all()
        return len(reviews)

    def get_reading_list(self, user_name):
        user = self.get_user(user_name)
        return user.read_books

    def get_reading_list_length(self, user_name):
        pass

    def add_review_to_user(self, review, user_name):
        pass

    def add_read_book(self, book: Book, user: User):
        pass

    def remove_read_book(self, book: Book, user: User):
        pass

    def set_stored_url(self, url):
        self.__stored_url = url

    def get_stored_url(self):
        return self.__stored_url
