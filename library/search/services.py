from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher


class NonExistentBookException(Exception):
    pass


def is_author(search_term, repo: AbstractRepository):
    authors = repo.get_authors()
    for author in authors:
        if search_term in author.full_name:
            return True
    return False


def is_publisher(search_term, repo: AbstractRepository):
    publishers = repo.get_publishers()
    for publisher in publishers:
        if search_term in publisher.name:
            return True
    return False


def is_release_year(search_term, repo: AbstractRepository):
    release_years = repo.get_release_years()

    try:
        int(search_term)
    except:
        return False
    else:
        if int(search_term) in release_years:
            return True
        else:
            return False


def is_title(search_term, repo:AbstractRepository):
    book_list = repo.get_all_books()
    for book in book_list:
        if search_term in book.title:
            return True
    return False
