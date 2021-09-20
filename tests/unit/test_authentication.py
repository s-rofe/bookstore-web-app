import pytest
from library.domain.model import User
from library.adapters.repository import RepositoryException
import library.authentication.services as services
from werkzeug.security import generate_password_hash, check_password_hash


def test_add_user(in_memory_repo):
    assert services.get_user("test1", in_memory_repo)