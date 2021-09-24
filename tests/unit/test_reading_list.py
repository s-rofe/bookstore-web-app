import pytest
import library.reading_list.services as services


def test_read_a_book(in_memory_repo):
    book = in_memory_repo.get_book_by_id(11827783)
    user = in_memory_repo.get_user("test1")
    in_memory_repo.add_read_book(book, user)
    assert book in services.get_reading_list('test1', in_memory_repo)


def test_remove_read_book(in_memory_repo):
    book = in_memory_repo.get_book_by_id(11827783)
    user = in_memory_repo.get_user("test1")
    in_memory_repo.add_read_book(book, user)
    assert book in services.get_reading_list('test1', in_memory_repo)
    in_memory_repo.remove_read_book(book, user)
    assert book not in services.get_reading_list('test1', in_memory_repo)


def test_get_reading_list_length(in_memory_repo):
    assert in_memory_repo.get_reading_list_length('test1') == 1
    book = in_memory_repo.get_book_by_id(11827783)
    user = in_memory_repo.get_user("test1")
    in_memory_repo.add_read_book(book, user)
    assert in_memory_repo.get_reading_list_length('test1') == 2