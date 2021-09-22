from werkzeug.security import generate_password_hash, check_password_hash
from library.adapters.repository import AbstractRepository
from library.domain.model import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass


def add_user(user_name, password, repo: AbstractRepository):
    # check if username is unique
    user = repo.get_user(user_name)
    if user is not None:
        raise NameNotUniqueException

    # Hash the password for security
    password_hashed = generate_password_hash(password)

    # Add the user instance to the repo
    user = User(user_name, password_hashed)
    repo.add_user(user)


def get_user(user_name, repo: AbstractRepository):
    user = repo.get_user(user_name)
    # Check if user exists
    if user is None:
        raise UnknownUserException
    return user


def authenticate_user(user_name, password, repo: AbstractRepository):
    user = repo.get_user(user_name)
    auth = False

    if user is not None:
        auth = check_password_hash(user.password, password)
    if not auth:
        raise AuthenticationException


def set_stored_url(url, repo: AbstractRepository):
    repo.set_stored_url(url)


def get_stored_url(repo: AbstractRepository):
    return repo.get_stored_url()
