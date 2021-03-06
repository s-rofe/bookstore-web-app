from library.adapters.repository import AbstractRepository


class NonExistentBookException(Exception):
    pass


def get_book_by_id(book_id: int, repo: AbstractRepository):
    book = repo.get_book_by_id(book_id)

    if book is None:
        raise NonExistentBookException

    return book


def get_all_books(repo: AbstractRepository):
    return repo.get_all_books()


def get_page_of_books(cursor, books_per_page, repo: AbstractRepository, book_list=None):
    if book_list is None:
        books = repo.get_page_of_books(cursor, books_per_page)
    else:
        books = repo.get_page_of_books(cursor, books_per_page, book_list)
    return books


def get_number_of_books(repo: AbstractRepository):
    return repo.get_number_of_books()


def get_books_with_publisher(publisher, repo: AbstractRepository):
    return repo.get_books_with_publisher(publisher)


def get_books_with_author(author, repo: AbstractRepository):
    # Author here is the name of the author as a string, not an object Author
    return repo.get_books_with_author(author)


def get_books_with_title(title, repo: AbstractRepository):
    return repo.get_books_by_title(title)


def get_books_with_release_year(release_year, repo: AbstractRepository):
    return repo.get_books_with_release_year(release_year)


def get_review_count(book_id, repo: AbstractRepository):
    return repo.get_review_count(book_id)
