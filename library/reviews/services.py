from typing import Iterable

from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher, Review, User


class NonExistentBookException(Exception):
    pass


def get_reviews(book_id, repo: AbstractRepository):
    return repo.get_reviews(book_id)


def get_book_by_id(book_id, repo: AbstractRepository):
    return repo.get_book_by_id(book_id)


def add_review(book_id, review_text, rating, user_name, repo: AbstractRepository):
    user = repo.get_user(user_name)
    book = repo.get_book_by_id(book_id)
    review = Review(book, review_text, rating)
    repo.add_review(review)
    # Add the review to the user's list of reviews
    user.add_review(review)
    repo.increase_review_count(book_id, 1)
