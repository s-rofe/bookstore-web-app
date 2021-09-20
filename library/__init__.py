"""Initialize Flask app."""

from flask import Flask, render_template
from pathlib import Path
import library.adapters.repository as repo
from library.adapters.jsondatareader import BooksJSONReader
from library.adapters.memory_repository import MemoryRepository, populate
from library.domain.model import Book


# TODO: Access to the books should be implemented via the repository pattern and using blueprints, so this can not stay here!
def create_some_book():
    some_book = Book(1, "Harry Potter and the Chamber of Secrets")
    some_book.description = "Ever since Harry Potter had come home for the summer, the Dursleys had been so mean \
                             and hideous that all Harry wanted was to get back to the Hogwarts School for \
                             Witchcraft and Wizardry. But just as he’s packing his bags, Harry receives a \
                             warning from a strange impish creature who says that if Harry returns to Hogwarts, \
                             disaster will strike."
    some_book.release_year = 1999
    return some_book


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Gets correct path of the JSON data files
    book_data_path = Path('library/adapters/data/comic_books_excerpt.json')
    author_data_path = Path('library/adapters/data/book_authors_excerpt.json')
    read_books = BooksJSONReader(book_data_path, author_data_path)
    if author_data_path.is_file() and book_data_path.is_file():
        read_books.read_json_files()
    else:
        print("Data files not found")

    # Create the repo object and populate it (for now only does books)
    repo.repo_instance = MemoryRepository()
    populate(read_books.dataset_of_books, repo.repo_instance)

    with app.app_context():
        # Register blueprints.
        from .book import book
        app.register_blueprint(book.book_blueprint)
        from .search import search
        app.register_blueprint(search.search_blueprint)
        from .home import home
        app.register_blueprint(home.home_blueprint)
        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)
        from .reviews import reviews
        app.register_blueprint(reviews.reviews_blueprint)
        from .reading_list import reading_list
        app.register_blueprint(reading_list.reading_list_blueprint)

    return app
