from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym

from library.domain import model


metadata = MetaData()

author_table = Table()

book_table = Table()

publisher_table = Table()

review_table = Table()

user_table = Table()


def map_model_to_tables():
    pass

