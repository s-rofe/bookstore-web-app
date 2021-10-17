from sqlalchemy import (
    Table, MetaData, Column, Integer, String, DateTime,
    ForeignKey, Boolean
)
from sqlalchemy.orm import mapper, relationship

from library.domain.model import Author, Publisher, Book, Review, User


metadata = MetaData()

authors_table = Table(
    'authors', metadata,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(255), nullable=False),
    Column('co_authors', ForeignKey('authors.id'))
)

books_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('description', String(1024)),
    Column('book_publisher', ForeignKey('publishers.id')),
    Column('book_authors', ForeignKey('authors.id')),
    Column('release_year', Integer),
    Column('ebook', Boolean),
    Column('num_pages', Integer),
    Column('total_ratings', Integer)
)

publishers_table = Table(
    'publishers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
)

reviews_table = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('reviewed_book', ForeignKey('books.id')),
    #Column('users', ForeignKey('users.id')),
    # we dont needs author ID?
    Column('review_text', String(1024), nullable=False),
    Column('rating', Integer, nullable=False),
    Column('author', ForeignKey('users.user_name')),
    Column('timestamp', DateTime, nullable=False)
)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('read_books', ForeignKey('books.id')),
    # Column('reviews', ForeignKey('reviews.id')),
    Column('pages_read', Integer, nullable=False)
)

book_authors_table = Table(
    'book_authors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('book_id', ForeignKey('books.id')),
    Column('author_id', ForeignKey('authors.id'))
)
user_reading_list = Table(
    'user_reading_list', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('book_id', ForeignKey('books.id'))
)


def map_model_to_tables():
    mapper(Author, authors_table, properties={
        '_Author__unique_id': authors_table.columns.id,
        '_Author__full_name': authors_table.columns.full_name,
        # One author can have many co_authors, 0, 1 - many?
        # '_Author__authors_this_one_has_worked_with': relationship(Author)
    })

    mapper(Book, books_table, properties={
        '_Book__book_id': books_table.columns.id,
        '_Book__title': books_table.columns.title,
        '_Book__description': books_table.columns.description,
        # Book can have 0 or 1 publisher but publisher doesnt store its books
        # Book can have many authors, authors can have many books...but authors dont store their books
        # So no back populates?
        '_Book__publisher': relationship(Publisher),
        '_Book__authors': relationship(Author, secondary=book_authors_table),
        '_Book__release_year': books_table.columns.release_year,
        '_Book__ebook': books_table.columns.ebook,
        '_Book__num_pages': books_table.columns.num_pages,
        '_Book__total_ratings': books_table.columns.total_ratings,
    })

    mapper(Publisher, publishers_table, properties={
        '_Publisher__name': publishers_table.columns.name,
    })

    mapper(Review, reviews_table, properties={
        #'_Review__book': relationship(Book),
        '_Review__review_text': reviews_table.columns.review_text,
        '_Review__rating': reviews_table.columns.rating,
        # '_Review__author': reviews_table.columns.author,
        '_Review__timestamp': reviews_table.columns.timestamp
    })

    mapper(User, users_table, properties={
        '_User__user_name': users_table.columns.user_name,
        '_User__password': users_table.columns.password,
        '_User__read_books': relationship(Book, secondary=user_reading_list),
        # ?????
        '_User__reviews': relationship(Review, backref='_Review__author'),
        '_User__pages_read': users_table.columns.pages_read
    })