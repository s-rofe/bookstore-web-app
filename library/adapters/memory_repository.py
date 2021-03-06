from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher, User, Review
from library.adapters.jsondatareader import BooksJSONReader
from werkzeug.security import generate_password_hash
from pathlib import Path
import csv
from utils import get_project_root


class MemoryRepository(AbstractRepository):

    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__books = list()
        self.__authors = list()
        self.__publishers = list()
        self.__release_years = list()
        self.__users = list()
        self.__reviews = list()
        self.__stored_url = None

    # testing
    def get_all_books(self):
        return self.__books

    def add_book(self, book: Book):
        self.__books.append(book)

    def add_author(self, author: Author):
        self.__authors.append(author)

    def get_authors(self):
        return self.__authors

    def add_publisher(self, publisher: Publisher):
        self.__publishers.append(publisher)

    def get_publishers(self):
        return self.__publishers

    def add_release_year(self, release_year):
        self.__release_years.append(release_year)

    def get_release_years(self):
        return self.__release_years

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name):
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_review(self, review: Review):
        self.__reviews.append(review)

    def get_reviews(self, book_id):
        books_reviews = [review for review in self.__reviews if review.book.book_id == book_id]
        return books_reviews

    def get_book_by_id(self, id: int):
        return next((book for book in self.__books if book.book_id == id), None)

    def get_number_of_books(self):
        return len(self.__books)

    def get_page_of_books(self, cursor, books_per_page, book_list=None):
        if book_list is None:
            book_list = self.__books
        if cursor * books_per_page + books_per_page >= len(self.__books):
            return book_list[cursor * books_per_page:]
        else:
            return book_list[cursor * books_per_page: cursor * books_per_page + books_per_page]

    def get_books_with_author(self, author_name):
        # For each books authors, if there is an author named the same as the author name passed, add it to the list
        author_name = author_name.lower()
        book_list = []
        for book in self.__books:
            for author in book.authors:
                author_db_name = author.full_name.lower()
                if author_name in author_db_name:
                    book_list.append(book)
        return book_list

    def get_books_with_publisher(self, publisher_name):
        book_list = []
        publisher_name = publisher_name.lower()
        for book in self.__books:
            pub_name = book.publisher.name.lower()
            if publisher_name in pub_name:
                book_list.append(book)
        return book_list

    def get_books_by_title(self, title):
        book_list = []
        title = title.lower()
        for book in self.__books:
            book_title = book.title.lower()
            if title in book_title:
                book_list.append(book)
        return book_list

    def get_books_with_release_year(self, release_year):
        book_list = [book for book in self.__books if book.release_year == release_year]
        return book_list

    def get_review_count(self, book_id):
        book = self.get_book_by_id(book_id)
        return book.total_ratings

    def increase_review_count(self, book_id, num):
        book = self.get_book_by_id(book_id)
        book.increase_total_ratings(num)

    def get_reading_list_length(self, user_name):
        user = self.get_user(user_name)
        return len(user.read_books)

    def get_reading_list(self, user_name):
        user = self.get_user(user_name)
        return user.read_books

    def add_review_to_user(self, review: Review, user: User):
        user.add_review(review)

    def add_read_book(self, book: Book, user: User):
        user.read_a_book(book)

    def remove_read_book(self, book: Book, user: User):
        user.remove_read_book(book)

    def set_stored_url(self, url):
        self.__stored_url = url

    def get_stored_url(self):
        return self.__stored_url


