import pytest
import library.reading_list.services as services
from library.domain.model import Book, User


def test_reading_list(in_memory_repo):
    book = in_memory_repo.get_book_by_id(11827783)
    user = in_memory_repo.get_user("test1")
    assert in_memory_repo.get_reading_list_length('test1') == 0
    in_memory_repo.add_read_book(book, user)
    assert in_memory_repo.get_reading_list_length('test1') == 1