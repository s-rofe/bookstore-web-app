import pytest

import datetime

from sqlalchemy.exc import IntegrityError

from library.domain.model import User, Book, Publisher, Author, Review


def make_user():
    user = User("Andrew", "Andrew123")
    return user


def insert_user(empty_session, values=None):
    new_name = "Andrew"
    new_password = "1234"

    if values is not None:
        new_name = values[0]
        new_password = values[1]

    empty_session.execute('INSERT INTO users (user_name, password) VALUES (:user_name, :password)',
                          {'user_name': new_name, 'password': new_password})
    row = empty_session.execute('SELECT id from users where user_name = :user_name',
                                {'user_name': new_name}).fetchone()
    return row[0]


def insert_users(empty_session, values):
        for value in values:
            empty_session.execute('INSERT INTO users (user_name, password, pages_read) VALUES (:user_name, :password, 0)',
                                  {'user_name': value[0], 'password': value[1]})
        rows = list(empty_session.execute('SELECT id from users'))
        keys = tuple(row[0] for row in rows)
        return keys


def make_book():
    books = Book(
        123,"Book Test"
    )
    return books


def insert_book(empty_session):
    empty_session.execute(
        'INSERT INTO books (id, title ) VALUES '
        '("123","Book Test")',

    )
    row = empty_session.execute('SELECT id from books').fetchone()
    return row[0]


def make_author():
    author = Author(123, "Bob Pancakes")
    return author


def insert_author(empty_session):
    empty_session.execute('INSERT INTO authors (id, full_name) VALUES (123, "Bob Pancakes")')
    row = empty_session.execute('SELECT id from authors').fetchone()
    return row


def insert_reviewed_book(empty_session):
    book_key = insert_book(empty_session)
    user_key = insert_user(empty_session)

    timestamp_1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timestamp_2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    empty_session.execute(
        'INSERT INTO reviews (author, reviewed_book, review_text, rating, timestamp) VALUES '
        '(:author, :reviewed_book, "Comment 1", "3", :timestamp_1),'
        '(:author, :reviewed_book, "Comment 2", "3", :timestamp_2)',
        {'author': user_key, 'reviewed_book': book_key, 'timestamp_1': timestamp_1, 'timestamp_2': timestamp_2}
    )

    row = empty_session.execute('SELECT id from books').fetchone()
    return row[0]


def test_loading_of_users(empty_session):
    users = list()
    users.append(("andrew", "1234"))
    users.append(("cindy", "1111"))
    insert_users(empty_session, users)

    expected = [
        User("Andrew", "1234"),
        User("Cindy", "999")
    ]
    assert empty_session.query(User).all() == expected


def test_saving_of_users(empty_session):
    user = User("Andrew2", "Andrew22")
    empty_session.add(user)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT user_name, password FROM users'))
    assert rows == [("andrew2", "Andrew22")]


def test_saving_of_users_with_common_user_name(empty_session):
    insert_user(empty_session, ("Andrew", "1234"))
    empty_session.commit()

    with pytest.raises(IntegrityError):
        user = User("Andrew", "111")
        empty_session.add(user)
        empty_session.commit()


def test_loading_of_book(empty_session):
    book_key = insert_book(empty_session)
    expected_book = make_book()
    fetched_book = empty_session.query(Book).one()

    assert expected_book == fetched_book
    assert book_key == fetched_book.book_id


def test_loading_of_reviewed_book(empty_session):
    insert_reviewed_book(empty_session)

    rows = empty_session.query(Book).all()
    book = rows[0]

    #for review in book.review:
    assert book is book


def test_saving_of_books(empty_session):
    book = make_book()
    empty_session.add(book)
    empty_session.commit()
    rows = list(empty_session.execute('SELECT id, title  FROM books'))
    assert rows == [(123,"Book Test")]


def test_save_reviewed_book(empty_session):
    # Create book User objects.
    book = make_book()
    user = make_user()
    rating = 1

    # Create a new Comment that is bidirectionally linked with the User and Article.
    review_text = "Some comment text."
    comment = Review(book, review_text, rating, user)

    # Save the new Article.
    empty_session.add(book)
    empty_session.add(user)
    empty_session.add(comment)
    empty_session.commit()

    # Test test_saving_of_article() checks for insertion into the articles table.
    rows = list(empty_session.execute('SELECT id FROM books'))
    book_key = rows[0][0]

    # Test test_saving_of_users() checks for insertion into the users table.
    rows = list(empty_session.execute('SELECT * FROM users'))
    user_key = rows[0][0]

    # Check that the comments table has a new record that links to the articles and users
    # tables.
    rows = list(empty_session.execute('SELECT reviewed_book, review_text FROM reviews'))
    assert rows == [(book_key, review_text)]
