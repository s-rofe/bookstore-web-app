import pytest

from pathlib import Path
from library.adapters.memory_repository import MemoryRepository, populate
from library.adapters.jsondatareader import BooksJSONReader
from utils import get_project_root



@pytest.fixture
def in_memory_repo():
    book_data_path = Path(get_project_root()) / 'library' / 'adapters' / 'data' / 'comic_books_excerpt.json'
    author_data_path = Path(get_project_root()) / 'library' / 'adapters' / 'data' / 'book_authors_excerpt.json'
    read_books = BooksJSONReader(book_data_path, author_data_path)
    if author_data_path.is_file() and book_data_path.is_file():
        read_books.read_json_files()
    else:
        print("Data files not found")

    # Create the repo object and populate it
    repo = MemoryRepository()
    populate(read_books.dataset_of_books, repo)
    return repo
