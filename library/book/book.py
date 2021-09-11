from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

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

    book_dict = services.get_page_of_books(cursor, books_per_page, repo.repo_instance)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('book_bp.browse_all_books', cursor=cursor - 1)
        first_book_page_url = url_for('book_bp.browse_all_books')

    if cursor * books_per_page < total_books:
        next_book_page_url = url_for('book_bp.browse_all_books', cursor=cursor + 1)

        last_cursor = (total_books // books_per_page) - 1
        last_book_page_url = url_for('book_bp.browse_all_books', cursor=last_cursor)

    return render_template(
        'books/browsebooks.html',
        title='All Books',
        books=book_dict,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )
