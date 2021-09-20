import pytest
import library.reviews.services as services
from library.domain.model import Book, Review


def test_get_reviews(in_memory_repo):
    assert len(in_memory_repo.get_reviews(27036539)) == 1
    services.add_review(27036539, "testing-testing", 4, "test1", in_memory_repo)
    assert len(in_memory_repo.get_reviews(27036539)) == 2
