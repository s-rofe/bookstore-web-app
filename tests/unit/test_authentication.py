import pytest
from library.domain.model import User
from library.adapters.repository import RepositoryException
import library.authentication.services as services
from library.authentication.services import AuthenticationException, UnknownUserException, NameNotUniqueException
from werkzeug.security import generate_password_hash, check_password_hash


def test_add_user(in_memory_repo):
    with pytest.raises(NameNotUniqueException):
        services.add_user('test1', 'Qwer5tyty', in_memory_repo)
    services.add_user('test8', "P0iutyty", in_memory_repo)
    assert services.get_user('test8', in_memory_repo)


def test_get_user(in_memory_repo):
    with pytest.raises(UnknownUserException):
        services.get_user('hahahahaha', in_memory_repo)
    assert services.get_user("test1", in_memory_repo) != UnknownUserException


def test_authenticate_user(in_memory_repo):
    auth = services.authenticate_user('test1', 'Test1@abc', in_memory_repo)
    assert auth != AuthenticationException
    with pytest.raises(AuthenticationException):
        services.authenticate_user('test1', 'testabc', in_memory_repo)
