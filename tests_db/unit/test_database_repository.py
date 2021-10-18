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


def test_publishers(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    pub = Publisher("Testpub")
    repo.add_publisher(pub)
    pubs = repo.get_publishers()
    assert pubs is not None and pub != []
    print(pubs)
    assert pubs.index(pub) != ValueError


def test_get_authors(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    auth = Author(99999, "Bob Pancakes")
    repo.add_author(auth)
    authors = repo.get_authors()
    assert authors is not None and authors != []
    assert authors.index(auth) != ValueError


def test_add_author(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    auth = Author(99998, "Eliza Pancakes")
    repo.add_author(auth)
    authors = repo.get_authors()
    assert authors.index(auth) != ValueError


def test_get_release_years(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    release_years = repo.get_release_years()
    assert release_years is not None and release_years != []


def test_load_users(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    assert repo.get_user("test1")
    assert repo.get_user("test2")
    assert repo.get_user("test3")


def test_add_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = User("test4", "Test4@abc")
    repo.add_user(user)
    assert repo.get_user("test4")


def test_get_add_reviews(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book1 = repo.get_book_by_id(27036539)
    review = Review(book1, "This is a test review", 4, "test3")
    repo.add_review(review)
    book_reviews = repo.get_reviews(27036539)
    assert book_reviews.index(review)


def test_get_all_books(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    all_books = repo.get_all_books()
    book1 = repo.get_book_by_id(27036539)
    assert all_books is not None and all_books != []
    assert all_books.index(book1) != ValueError


def test_get_book_by_id(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book1 = repo.get_book_by_id(27036539)
    assert book1 is not None


def test_get_number_of_books(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    num_of_books = repo.get_number_of_books()
    assert num_of_books == 20


def test_get_page_of_books(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book_list = repo.get_all_books()
    book_list_one = repo.get_page_of_books(0, 4)
    assert len(book_list_one) == 4
    book_section_one = repo.get_page_of_books(1, 4)
    assert book_list[4] == book_section_one[0]
    assert book_list[7] == book_section_one[-1]


def test_get_books_with_author(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book_by_author = repo.get_books_with_author("Tomas Aira")
    book_section_zero = repo.get_page_of_books(0, 4, book_by_author)
    assert book_by_author[0] == book_section_zero[0]
    assert book_by_author[-1] == book_section_zero[-1]


def test_get_books_with_publisher(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book_by_pub = repo.get_books_with_publisher("N/A")
    book_section_zero = repo.get_page_of_books(0, 4, book_by_pub)
    assert book_by_pub[0] == book_section_zero[0]
    assert book_by_pub[3] == book_section_zero[-1]
    book_section_one = repo.get_page_of_books(1, 4, book_by_pub)
    assert book_by_pub[-1] == book_section_one[0]
    assert len(book_section_one) == 1


def test_get_books_with_release_year(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book_by_year = repo.get_books_with_release_year(2016)
    book_section_zero = repo.get_page_of_books(0, 4, book_by_year)
    assert book_by_year[0] == book_section_zero[0]
    assert book_by_year[3] == book_section_zero[-1]
    book_section_one = repo.get_page_of_books(1, 4, book_by_year)
    assert book_by_year[-1] == book_section_one[0]
    assert len(book_section_one) == 1


def test_get_books_by_title(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book_list = repo.get_books_by_title("Volume")
    assert len(book_list) == 6


def test_add_review_to_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book = repo.get_book_by_id(27036539)
    user = repo.get_user("test1")
    review1 = Review(book, "This is a test", 2, user.user_name)
    repo.add_review(review1)
    user.add_review(review1)
    assert user.reviews.index(review1) != ValueError


def test_load_reviews(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    assert repo.get_book_by_id(27036539)
    assert len(repo.get_reviews(27036539)) == 4
    assert len(repo.get_reviews(27036537)) == 1
    assert len(repo.get_reviews(27036536)) == 2
    # book id 27036539 author Tomas Aira 27036537 27036536


def test_get_reading_list(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    reading_list = repo.get_reading_list("test1")
    assert reading_list != []


def test_get_reading_list_length(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    reading_list = repo.get_reading_list_length("test1")
    assert reading_list == 1


def test_remove_read_book(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = repo.get_user("test1")
    book = repo.get_book_by_id(27036539)
    repo.add_read_book(book, user)
    assert repo.get_reading_list_length("test1") == 2
    repo.remove_read_book(book, user)
    assert repo.get_reading_list_length("test1") == 1


def test_add_read_book(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    book1 = repo.get_book_by_id(27036539)
    user1 = repo.get_user("test1")
    repo.add_read_book(book1, user1)
    reading_list = repo.get_reading_list("test1")
    assert reading_list.index(book1) != ValueError



