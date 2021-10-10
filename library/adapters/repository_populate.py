from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher, User, Review
from library.adapters.jsondatareader import BooksJSONReader
from werkzeug.security import generate_password_hash
from pathlib import Path
import csv
from utils import get_project_root


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
            author=data_row[4]
        )
        repo.add_review(review)


def load_json_data(book_dataset, repo):
    for book in book_dataset:
        repo.add_book(book)
        for author in book.authors:
            repo.add_author(author)
        repo.add_publisher(book.publisher)
        repo.add_release_year(book.release_year)


def populate(data_path, repo):
    # Get the dataset of books from the json files
    book_data_path = Path(data_path) / "comic_books_excerpt.json"
    author_data_path = Path(data_path) / "book_authors_excerpt.json"
    read_books = BooksJSONReader(book_data_path, author_data_path)
    if author_data_path.is_file() and book_data_path.is_file():
        read_books.read_json_files()

    # Load the data
    load_json_data(read_books.dataset_of_books, repo)
    load_users(repo)
    load_reviews(repo)

    # give user test1 a book in the reading list for testing
    book = repo.get_book_by_id(25742454)
    user = repo.get_user("test1")
    repo.add_read_book(book, user)
