from flask import Blueprint
from flask import request, render_template, url_for

import library.adapters.repository as repo
import library.book.services as services

book_blueprint = Blueprint("book_bp", __name__)


@book_blueprint.route('/browse_all_books', methods=['GET'])
def browse_all_books():
    books_per_page = 4
    cursor = request.args.get('cursor')
    total_books = services.get_number_of_books(repo.repo_instance)

    # cursor to section the books to be displayed from the list
    if cursor is None:
        # If no cursor set up yet, initialize cursor to start at the beginning
        cursor = 0
    else:
        cursor = int(cursor)

    book_list = services.get_page_of_books(cursor, books_per_page, repo.repo_instance)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('book_bp.browse_all_books', cursor=cursor - 1)
        first_book_page_url = url_for('book_bp.browse_all_books')

    if cursor * books_per_page + books_per_page < total_books:
        next_book_page_url = url_for('book_bp.browse_all_books', cursor=cursor + 1)

        last_cursor = (total_books // books_per_page) - 1
        last_book_page_url = url_for('book_bp.browse_all_books', cursor=last_cursor)

    return render_template(
        'books/browsebooks.html',
        title='All Books',
        books=book_list,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )


@book_blueprint.route('/books_by_author/<author_name>', methods=['GET'])
def books_by_author(author_name):
    books_per_page = 4
    cursor = request.args.get('cursor')

    # cursor to section the books to be displayed from the list
    if cursor is None:
        # If no cursor set up yet, initialize cursor to start at the beginning
        cursor = 0
    else:
        cursor = int(cursor)

    book_list = services.get_books_with_author(author_name, repo.repo_instance)
    total_books = len(book_list)
    books_by_page = services.get_page_of_books(cursor, books_per_page, repo.repo_instance, book_list)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('book_bp.books_by_author', author_name=author_name, cursor=cursor - 1)
        first_book_page_url = url_for('book_bp.books_by_author', author_name=author_name)

    if cursor * books_per_page + books_per_page < total_books:
        next_book_page_url = url_for('book_bp.books_by_author', author_name=author_name, cursor=cursor + 1)

        last_cursor = (total_books // books_per_page) - 1
        last_book_page_url = url_for('book_bp.books_by_author', author_name=author_name, cursor=last_cursor)

    return render_template(
        'books/browsebooks.html',
        title='Books',
        books_title='Books by ' + author_name,
        books=books_by_page,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )


@book_blueprint.route('/books_by_publisher/<publisher_name>', methods=['GET'])
def books_by_publisher(publisher_name):
    books_per_page = 4
    cursor = request.args.get('cursor')

    # cursor to section the books to be displayed from the list
    if cursor is None:
        # If no cursor set up yet, initialize cursor to start at the beginning
        cursor = 0
    else:
        cursor = int(cursor)

    book_list = services.get_books_with_publisher(publisher_name, repo.repo_instance)
    total_books = len(book_list)
    books_by_page = services.get_page_of_books(cursor, books_per_page, repo.repo_instance, book_list)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('book_bp.books_by_publisher', publisher_name=publisher_name, cursor=cursor - 1)
        first_book_page_url = url_for('book_bp.books_by_publisher', publisher_name=publisher_name)

    if cursor * books_per_page + books_per_page < total_books:
        next_book_page_url = url_for('book_bp.books_by_publisher', publisher_name=publisher_name, cursor=cursor + 1)

        last_cursor = (total_books // books_per_page) - 1
        last_book_page_url = url_for('book_bp.books_by_publisher', publisher_name=publisher_name, cursor=last_cursor)

    return render_template(
        'books/browsebooks.html',
        title='Books',
        books_title='Books Published by ' + publisher_name,
        books=books_by_page,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )


@book_blueprint.route('/books_by_release_year/<release_year>', methods=['GET'])
def books_by_release_year(release_year):
    books_per_page = 4
    cursor = request.args.get('cursor')

    # cursor to section the books to be displayed from the list
    if cursor is None:
        # If no cursor set up yet, initialize cursor to start at the beginning
        cursor = 0
    else:
        cursor = int(cursor)

    book_list = services.get_books_with_release_year(int(release_year), repo.repo_instance)
    total_books = len(book_list)
    books_by_page = services.get_page_of_books(cursor, books_per_page, repo.repo_instance, book_list)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('book_bp.books_by_release_year', release_year=release_year, cursor=cursor - 1)
        first_book_page_url = url_for('book_bp.books_by_release_year', release_year=release_year)

    if cursor * books_per_page + books_per_page < total_books:
        next_book_page_url = url_for('book_bp.books_by_release_year', release_year=release_year, cursor=cursor + 1)

        last_cursor = (total_books // books_per_page) - 1
        last_book_page_url = url_for('book_bp.books_by_release_year', release_year=release_year, cursor=last_cursor)

    return render_template(
        'books/browsebooks.html',
        title='Books',
        books_title='Books by year ' + release_year,
        books=books_by_page,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )


@book_blueprint.route('/books_by_title/<title>', methods=['GET'])
def books_by_title(title):
    books_per_page = 4
    cursor = request.args.get('cursor')

    # cursor to section the books to be displayed from the list
    if cursor is None:
        # If no cursor set up yet, initialize cursor to start at the beginning
        cursor = 0
    else:
        cursor = int(cursor)

    book_list = services.get_books_with_title(title, repo.repo_instance)
    total_books = len(book_list)
    books_by_page = services.get_page_of_books(cursor, books_per_page, repo.repo_instance, book_list)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('book_bp.books_by_title', title=title, cursor=cursor - 1)
        first_book_page_url = url_for('book_bp.browse_by_title', title=title)

    if cursor * books_per_page + books_per_page < total_books:
        next_book_page_url = url_for('book_bp.books_by_title', title=title, cursor=cursor + 1)

        last_cursor = (total_books // books_per_page)
        last_book_page_url = url_for('book_bp.books_by_title', title=title, cursor=last_cursor)

    return render_template(
        'books/browsebooks.html',
        title='Books',
        books_title='Books with title ' + title,
        books=books_by_page,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )
