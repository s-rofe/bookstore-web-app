from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher, User, Review
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
        book_list = []
        for book in self.__books:
            for author in book.authors:
                if author.full_name == author_name:
                    book_list.append(book)
        return book_list

    def get_books_with_publisher(self, publisher):
        book_list = []
        for book in self.__books:
            if book.publisher.name == publisher:
                book_list.append(book)
        return book_list

    def get_books_with_release_year(self, release_year):
        book_list = [book for book in self.__books if book.release_year == release_year]
        return book_list


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_users(repo):
    # User names are changed to lowercase in the model
    users_filename = Path(get_project_root()) / 'library' / 'adapters' / 'data' / 'users.csv'
    for data_row in read_csv_file(users_filename):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)


def load_reviews(repo):
    # User names are changed to lowercase in the model
    reviews_filename = Path(get_project_root()) / 'library' / 'adapters' / 'data' / 'reviews.csv'
    for data_row in read_csv_file(reviews_filename):
        review = Review(
            book=repo.get_book_by_id(int(data_row[1])),
            review_text=data_row[2],
            rating=int(data_row[3]),
        )
        repo.add_review(review)


def populate(book_dataset, repo):
    for book in book_dataset:
        repo.add_book(book)
        for author in book.authors:
            repo.add_author(author)
        repo.add_publisher(book.publisher)
        repo.add_release_year(book.release_year)
    load_users(repo)
    load_reviews(repo)
