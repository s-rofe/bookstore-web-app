from library.adapters.repository import AbstractRepository
from library.domain.model import Book, Author, Publisher


class MemoryRepository(AbstractRepository):

    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__books = list()
        self.__authors = list()
        self.__publishers = list()
        self.__release_years = list()

    # testing
    def get_all_books(self):
        return self.__books

    def add_book(self, book: Book):
        self.__books.append(book)

    def add_author(self, author: Author):
        self.__authors.append(author)

    def get_authors(self):
        return self.__authors

    def add_publisher(self, publisher: Publisher):
        self.__publishers.append(publisher)

    def get_publishers(self):
        return self.__publishers

    def add_release_year(self, release_year):
        self.__release_years.append(release_year)

    def get_release_years(self):
        return self.__release_years

    def get_book_by_id(self, id: int):
        return next((book for book in self.__books if book.book_id == id), None)

    def get_number_of_books(self):
        return len(self.__books)

    def get_page_of_books(self, cursor, books_per_page, book_list=None):
        if book_list is None:
            book_list = self.__books
        if cursor * books_per_page + books_per_page >= len(self.__books):
            return book_list[cursor * books_per_page:]
        else:
            return book_list[cursor * books_per_page: cursor * books_per_page + books_per_page]

    def get_books_with_author(self, author_name):
        # For each books authors, if there is an author named the same as the author name passed, add it to the list
        book_list = []
        for book in self.__books:
            for author in book.authors:
                if author.full_name == author_name:
                    book_list.append(book)
        return book_list

    def get_books_with_publisher(self, publisher):
        book_list = []
        for book in self.__books:
            if book.publisher.name == publisher:
                book_list.append(book)
        return book_list

    def get_books_with_release_year(self, release_year):
        book_list = [book for book in self.__books if book.release_year == release_year]
        return book_list


def populate(book_dataset, repo):
    for book in book_dataset:
        repo.add_book(book)
