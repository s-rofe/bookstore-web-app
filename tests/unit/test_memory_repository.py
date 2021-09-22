import pytest
from library.domain.model import Book, Review
from library.adapters.repository import RepositoryException


def test_books_in_repo(in_memory_repo):
    assert in_memory_repo.get_all_books() is not []


def test_get_number_of_books(in_memory_repo):
    assert in_memory_repo.get_number_of_books() == 20


def test_get_page_of_books(in_memory_repo):
    book_list = in_memory_repo.get_page_of_books(0, 4)
    assert len(book_list) == 4


def test_load_users(in_memory_repo):
    assert in_memory_repo.get_user("test1")
    assert in_memory_repo.get_user("test2")
    assert in_memory_repo.get_user("test3")


def test_load_reviews(in_memory_repo):
    assert in_memory_repo.get_book_by_id(27036539)
    assert len(in_memory_repo.get_reviews(27036539)) == 4
    assert len(in_memory_repo.get_reviews(27036537)) == 1
    assert len(in_memory_repo.get_reviews(27036536)) == 1
    # book id 27036539 author Tomas Aira 27036537 27036536


def test_remove_read_book(in_memory_repo):
    user = in_memory_repo.get_user("test1")
    book = in_memory_repo.get_book_by_id(27036539)
    in_memory_repo.add_read_book(book, user)
    assert in_memory_repo.get_reading_list_length("test1") == 1
    in_memory_repo.remove_read_book(book, user)
    assert in_memory_repo.get_reading_list_length("test1") == 0


