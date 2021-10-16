from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey, Boolean, Time
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapper, relationship, synonym

from library.domain.model import Author, Publisher, Book, Review


metadata = MetaData()

author_table = Table(
    'authors', metadata,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(255), nullable=False),
    Column('co_authors', ARRAY(Author), nullable=False)
)

book_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('description', String(1024)),
    Column('publisher', Publisher),
    Column('authors', ARRAY(Author), nullable=False),
    Column('release_year', Integer),
    Column('ebook', Boolean),
    Column('num_pages', Integer),
    Column('total_ratings', Integer, nullable=False)
)

publisher_table = Table(
    'publisher', metadata,
    Column('name', String(255), primary_key=True)
)

review_table = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('book', Book),
    Column('review_text', String(1024), nullable=False),
    Column('rating', Integer, nullable=False),
    Column('author', String(255)),
    Column('timestamp', Time, nullable=False)
)

user_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('read_books', ARRAY(Book), nullable=False),
    Column('reviews', ARRAY(Review), nullable=False),
    Column('pages_read', Integer, nullable=False)
)


def map_model_to_tables():
    pass

