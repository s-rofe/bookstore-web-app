import json
from typing import List

from library.domain.model import Publisher, Author, Book


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self) -> List[Book]:
        return self.__dataset_of_books

    def read_books_file(self) -> list:
        books_json = []
        with open(self.__books_file_name, encoding='UTF-8') as books_jsonfile:
            for line in books_jsonfile:
                book_entry = json.loads(line)
                books_json.append(book_entry)
        return books_json

    def read_authors_file(self) -> list:
        authors_json = []
        with open(self.__authors_file_name, encoding='UTF-8') as authors_jsonfile:
            for line in authors_jsonfile:
                author_entry = json.loads(line)
                authors_json.append(author_entry)
        return authors_json

    def read_json_files(self):
        try:
            book_file = open(self.__books_file_name, "r")
            author_file = open(self.__authors_file_name, "r")
        except FileNotFoundError:
            raise ValueError

        self.__dataset_of_books = []
        author_list = []
        for line in author_file:
            author_data = json.loads(line)
            temp_author = Author(int(author_data.get("author_id")), author_data.get("name"))
            author_list.append(temp_author)

        for line in book_file:
            data = json.loads(line)
            temp_book = Book(int(data.get("book_id")), data.get("title"))
            temp_book.description = data.get("description")
            temp_book.publisher = Publisher(data.get("publisher"))
            try:
                temp_book.release_year = int(data.get("publication_year"))
            except ValueError:
                pass
            if data.get("is_ebook") == "true":
                temp_book.ebook = True
            elif data.get("is_ebook") == "false":
                temp_book.ebook = False

            if data.get('num_pages') != "":
                temp_book.num_pages = int(data.get('num_pages'))
            if data.get('ratings_count') != "":
                temp_book.total_ratings = int(data.get('ratings_count'))

            authors = data.get("authors")
            author_ids = []
            for auth in authors:
                author_ids.append(int(auth.get("author_id")))

            for author in author_list:
                if author.unique_id in author_ids:
                    temp_book.add_author(author)
            self.__dataset_of_books.append(temp_book)

