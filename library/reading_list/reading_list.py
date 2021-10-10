from flask import Blueprint
from flask import request, render_template, url_for, session, redirect

import library.adapters.repository as repo
import library.reading_list.services as services
from library.authentication.authentication import login_required

reading_list_blueprint = Blueprint("reading_list_bp", __name__)


@reading_list_blueprint.route('/add_to_reading_list', methods=['GET', 'POST'])
@login_required
def add_to_reading_list():
    book_id = request.args.get('book_id')
    book = services.get_book_by_id(int(book_id), repo.repo_instance)
    user_name = session['user_name']
    user = services.get_user(user_name, repo.repo_instance)
    services.read_a_book(book, user, repo.repo_instance)
    reading_list_length = services.get_reading_list_length(user_name, repo.repo_instance)
    new_cursor = (reading_list_length - 1) // 4
    return redirect(url_for('reading_list_bp.reading_list', cursor=new_cursor))


@reading_list_blueprint.route('/remove_read_book', methods=['GET', 'POST'])
@login_required
def remove_read_book():
    book_id = request.args.get('book_id')
    book = services.get_book_by_id(int(book_id), repo.repo_instance)
    user_name = session['user_name']
    user = services.get_user(user_name, repo.repo_instance)
    services.remove_read_book(book, user, repo.repo_instance)
    reading_list_length = services.get_reading_list_length(user_name, repo.repo_instance)
    new_cursor = reading_list_length // 4
    return redirect(url_for('reading_list_bp.reading_list', cursor=new_cursor))


@reading_list_blueprint.route('/reading_list', methods=['GET'])
@login_required
def reading_list():
    books_per_page = 4
    cursor = request.args.get('cursor')
    user_name = session['user_name']

    # cursor to section the books to be displayed from the list
    if cursor is None:
        # If no cursor set up yet, initialize cursor to start at the beginning
        cursor = 0
    else:
        cursor = int(cursor)

    book_list = services.get_reading_list(user_name, repo.repo_instance)
    total_books = len(book_list)
    books_by_page = services.get_page_of_books(cursor, books_per_page, repo.repo_instance, book_list)

    first_book_page_url = None
    last_book_page_url = None
    next_book_page_url = None
    prev_book_page_url = None

    if cursor > 0:
        prev_book_page_url = url_for('reading_list_bp.reading_list', cursor=cursor - 1)
        first_book_page_url = url_for('reading_list_bp.reading_list')

    if cursor * books_per_page + books_per_page < total_books:
        next_book_page_url = url_for('reading_list_bp.reading_list', cursor=cursor + 1)

        last_cursor = (total_books // books_per_page)
        last_book_page_url = url_for('reading_list_bp.reading_list', cursor=last_cursor)

    return render_template(
        'reading_list/reading_list.html',
        title='Your reading list',
        books=books_by_page,
        user_name=user_name,
        first_book_page_url=first_book_page_url,
        last_book_page_url=last_book_page_url,
        next_book_page_url=next_book_page_url,
        prev_book_page_url=prev_book_page_url
    )