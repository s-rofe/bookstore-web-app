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


def test_get_books_by_attribute(in_memory_repo):
    book_list = in_memory_repo.get_all_books()
    books_with_author = book_services.get_books_with_author("Tomas Aira", in_memory_repo)
    assert len(books_with_author) == 2
    books_with_year = book_services.get_books_with_release_year(2016, in_memory_repo)
    assert len(books_with_year) == 5
    books_with_pub = book_services.get_books_with_publisher("Avatar Press", in_memory_repo)
    assert len(books_with_pub) == 4


def test_books_with_author(in_memory_repo):
    # No author has >4 books
    book_by_author = book_services.get_books_with_author("Tomas Aira", in_memory_repo)
    book_section_zero = book_services.get_page_of_books(0, 4, in_memory_repo, book_by_author)
    assert book_by_author[0] == book_section_zero[0]
    assert book_by_author[-1] == book_section_zero[-1]


def test_books_with_publisher(in_memory_repo):
    book_list = in_memory_repo.get_all_books()
    book_by_pub = book_services.get_books_with_publisher("N/A", in_memory_repo)
    book_section_zero = book_services.get_page_of_books(0, 4, in_memory_repo, book_by_pub)
    assert book_by_pub[0] == book_section_zero[0]
    assert book_by_pub[3] == book_section_zero[-1]
    book_section_one = book_services.get_page_of_books(1, 4, in_memory_repo, book_by_pub)
    assert book_by_pub[-1] == book_section_one[0]
    assert len(book_section_one) == 1


def test_books_with_release_year(in_memory_repo):
    book_by_year = book_services.get_books_with_release_year(2016, in_memory_repo)
    book_section_zero = book_services.get_page_of_books(0, 4, in_memory_repo, book_by_year)
    assert book_by_year[0] == book_section_zero[0]
    assert book_by_year[3] == book_section_zero[-1]
    book_section_one = book_services.get_page_of_books(1, 4, in_memory_repo, book_by_year)
    assert book_by_year[-1] == book_section_one[0]
    assert len(book_section_one) == 1



