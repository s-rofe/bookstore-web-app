import pytest
import library.reviews.services as services


def test_get_reviews(in_memory_repo):
    assert len(in_memory_repo.get_reviews(27036539)) == 4
    assert len(in_memory_repo.get_reviews(303030)) == 0


def test_add_review(in_memory_repo):
    services.add_review(27036539, "testing-testing", 4, "test1", in_memory_repo)
    assert len(in_memory_repo.get_reviews(27036539)) == 5