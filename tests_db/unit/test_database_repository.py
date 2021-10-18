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
    print(book1)
    assert book1.authors


def test_get_book_publisher(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book1 = repo.get_book_by_id(27036539)
    print(book1)
    assert book1.publisher


def test_books_in_repo(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    assert repo.get_all_books() is not []


def test_get_number_of_books(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    assert repo.get_number_of_books() == 20


def test_get_page_of_books(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book_list = repo.get_page_of_books(0, 4)
    assert len(book_list) == 4


def test_get_publisher(session_factory):
    pass


def test_add_publisher(session_factory):
    pass


def test_load_publishers(session_factory):
    pass


def test_get_author(session_factory):
    pass


def test_add_author(session_factory):
    pass


def test_get_author(session_factory):
    pass


def test_load_authors(session_factory):
    pass


def test_get_release_years(session_factory):
    pass


def test_load_users(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    assert repo.get_user("test1")
    assert repo.get_user("test2")
    assert repo.get_user("test3")


def test_add_a_user(session_factory):
    pass


def test_add_review(session_factory):
    pass


def test_get_review(session_factory):
    pass


def test_get_all_books(session_factory):
    pass


def test_get_book_by_id(session_factory):
    pass


def test_get_number_of_books(session_factory):
    pass


def test_get_page_of_books(session_factory):
    pass


def test_get_books_with_author(session_factory):
    pass


def test_get_books_with_publisher(session_factory):
    pass


def test_get_books_with_release_year(session_factory):
    pass


def test_get_books_by_title(session_factory):
    pass


def test_increase_review_count(session_factory):
    pass


def test_get_review_count(session_factory):
    pass


def test_add_review_to_user(session_factory):
    pass


def test_load_reviews(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    assert repo.get_book_by_id(27036539)
    assert len(repo.get_reviews(27036539)) == 4
    assert len(repo.get_reviews(27036537)) == 1
    assert len(repo.get_reviews(27036536)) == 2
    # book id 27036539 author Tomas Aira 27036537 27036536


def test_get_reading_list(session_factory):
    pass


def test_get_reading_list_length(session_factory):
    pass


def test_remove_read_book(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = repo.get_user("test1")
    book = repo.get_book_by_id(27036539)
    repo.add_read_book(book, user)
    assert repo.get_reading_list_length("test1") == 2
    repo.remove_read_book(book, user)
    assert repo.get_reading_list_length("test1") == 1


def test_add_read_book(session_factory):
    pass



