import pytest
from library.domain.model import Book
from library.adapters.repository import RepositoryException


def test_books_in_repo(in_memory_repo):
    assert in_memory_repo.get_all_books() is not []


def test_get_number_of_books(in_memory_repo):
    assert in_memory_repo.get_number_of_books() == 20


def test_get_page_of_books(in_memory_repo):
    book_list = in_memory_repo.get_page_of_books(0, 4)
    assert len(book_list) == 4
