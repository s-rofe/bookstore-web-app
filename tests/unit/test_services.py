import pytest
from library.book import services as book_services


def test_get_book_pages(in_memory_repo):
    book_list = in_memory_repo.get_all_books()
    # test section 0
    book_section_zero = book_services.get_page_of_books(0, 4, in_memory_repo)
    assert book_list[0] == book_section_zero[0]
    assert book_list[3] == book_section_zero[-1]
    # test section 1
    book_section_one = book_services.get_page_of_books(1, 4, in_memory_repo)
    assert book_list[4] == book_section_one[0]
    assert book_list[7] == book_section_one[-1]
