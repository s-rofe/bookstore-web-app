from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey, Boolean, Time
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapper, relationship, synonym

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
    Column('publisher', ForeignKey('publishers.id')),
    Column('authors', ForeignKey('authors.id')),
    Column('release_year', Integer),
    Column('ebook', Boolean),
    Column('num_pages', Integer),
    Column('total_ratings', Integer, nullable=False)
)

publishers_table = Table(
    'publishers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False)
)

reviews_table = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('book', ForeignKey('books.id')),
    Column('review_text', String(1024), nullable=False),
    Column('rating', Integer, nullable=False),
    Column('author', ForeignKey('users.user_name')),
    Column('timestamp', Time, nullable=False)
)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('read_books', ForeignKey('books.id')),
    Column('reviews', ForeignKey('reviews.id')),
    Column('pages_read', Integer, nullable=False)
)


def map_model_to_tables():
    pass
