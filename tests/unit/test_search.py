import pytest
from library.search import services


def test_is_author(in_memory_repo):
    assert services.is_author("Tomas Aira", in_memory_repo)
    assert not services.is_author("123", in_memory_repo)


def test_is_publisher(in_memory_repo):
    assert services.is_publisher("Avatar Press", in_memory_repo)
    assert not services.is_publisher("boo", in_memory_repo)


def test_is_release_year(in_memory_repo):
    assert services.is_release_year("2016", in_memory_repo)
    assert not services.is_release_year("a", in_memory_repo)