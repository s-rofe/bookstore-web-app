"""Initialize Flask app."""

from pathlib import Path

from flask import Flask

import library.adapters.repository as repo
from library.adapters.jsondatareader import BooksJSONReader
from library.adapters.memory_repository import MemoryRepository, populate
from library.domain.model import Book


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = Path('library') / 'adapters' / 'data'

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # Create the repo object and populate it (for now only does books)
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

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
