from library.adapters.repository import AbstractRepository


class NonExistentBookException(Exception):
    pass


def is_author(search_term, repo: AbstractRepository):
    search_term = search_term.lower()
    authors = repo.get_authors()
    for author in authors:
        author_name = author.full_name.lower()
        if search_term in author_name:
            return True
    return False


def is_publisher(search_term, repo: AbstractRepository):
    search_term = search_term.lower()
    publishers = repo.get_publishers()
    for publisher in publishers:
        pub_name = publisher.name.lower()
        if search_term in pub_name:
            return True
    return False


def is_release_year(search_term, repo: AbstractRepository):
    release_years = repo.get_release_years()

    try:
        int(search_term)
    except:
        return False
    else:
        if int(search_term) in release_years:
            return True
        else:
            return False


def is_title(search_term, repo: AbstractRepository):
    search_term = search_term.lower()
    book_list = repo.get_all_books()
    for book in book_list:
        book_title = book.title.lower()
        print(book.title.lower())
        if search_term in book_title:
            return True
    return False
