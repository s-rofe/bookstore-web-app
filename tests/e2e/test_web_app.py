import pytest
from flask import session


def test_register(client):
    # Check that the register page can be retrieved
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    # Check a user can be registered with valid inputs
    response = client.post(
        '/authentication/register',
        data={'user_name': 'test5', 'password': 'Test5@abc'}
    )
    # Check that a successful registration redirects to the login page
    assert response.location == 'http://localhost/authentication/login'


@pytest.mark.parametrize(('user_name', 'password', 'message'), (
        ('', '', b'Username is required'),
        ('bob', '', b'Username too short'),
        ('bob2', '', b'Password required'),
        ('bob2', 'abc', b'Password must be at least 8 characters long and contain upper case and lower case letters, ' \
                        b'and a digit'),
        ('test1', 'Test1@abc', b'Username taken - please try another'),
))
def test_register_with_invalid_input(client, user_name, password, message):
    # Check the above inputs, give the corresponding error messages
    response = client.post(
        '/authentication/register',
        data={'user_name': user_name, 'password': password}
    )
    print(response.data)
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the page prior to logging in.
    response = auth.login()
    # None for test cases
    assert response.location == 'http://localhost/authentication/None'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/')
        assert session['user_name'] == 'test1'


def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user session.
        auth.logout()
        assert 'user_id' not in session


def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Book Store where you can find all the books provided in the repository' in response.data


def test_login_required_to_review(client):
    response = client.post('/write_review')
    assert response.location == 'http://localhost/authentication/login'


def test_review(client, auth):
    # Login a user.
    auth.login()

    # Check that we can retrieve the reviews page.
    response = client.get('/reviews?book_id=25742454')

    response = client.post(
        '/write_review',
        data={'review': 'Best book to help get through lockdown', 'rating': 2, 'book_id': '25742454'}
    )
    # Checks that after writing review, user is redirected back to reviews page
    assert response.location == 'http://localhost/reviews?book_id=25742454'


@pytest.mark.parametrize(('review', 'messages'), (
        ('The main character is a assh*le', (b'Profanity is not allowed')),
        ('B', (b'Your review is too short')),
        ('ass', (b'Your review is too short', b'Profanity is not allowed')),
))
def test_review_with_invalid_input(client, auth, review, messages):
    # Login a user.
    auth.login()

    # Attempt to comment on an article.
    response = client.post(
        '/write_review',
        data={'review': review, 'rating': 2, 'book_id': '25742454'}
    )
    # Check that supplying invalid comment text generates appropriate error messages.
    for message in messages:
        assert message in response.data


def test_search_book_by_title(client):
    response = client.get('/books_by_title/?title=volume')
    assert response.status_code == 200

    assert b'War Stories, Volume 3' in response.data
    assert b'Crossed, Volume 15' in response.data


def test_search_book_by_author(client):
    response = client.get('/books_by_author?author_name=Tomas+Aira')
    assert response.status_code == 200

    assert b'War Stories, Volume 3' in response.data
    assert b'War Stories, Volume 4' in response.data


def test_search_book_by_publisher(client):
    response = client.get('/books_by_publisher?publisher_name=avatar')
    assert response.status_code == 200

    assert b'War Stories, Volume 3' in response.data
    assert b'Crossed, Volume 15' in response.data


def test_search_book_by_release_year(client):
    response = client.get('/books_by_release_year?release_year=2016')
    assert response.status_code == 200

    assert b'War Stories, Volume 3' in response.data
    assert b'Cruelle' in response.data


def test_reading_list(client, auth):
    auth.login()
    response = client.get('/reading_list')
    assert response.status_code == 200

    # Check reading list contains the sample book
    assert b'The Switchblade Mamma' in response.data
