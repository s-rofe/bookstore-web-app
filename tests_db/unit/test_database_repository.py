import pytest

import library.adapters.repository as repo
from library.adapters.database_repository import SqlAlchemyRepository
from library.domain.model import User, Book, Author, Review, Publisher
from library.adapters.repository import RepositoryException


def test_get_book(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book1 = repo.get_book_by_id(27036539)
    assert book1
    # assert book1.publisher


def test_get_book_author(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book1 = repo.get_book_by_id(27036539)
    assert book1.author