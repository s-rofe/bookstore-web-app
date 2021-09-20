from flask import Blueprint, redirect
from flask import render_template, url_for, request

import library.adapters.repository as repo
import library.search.services as services

search_blueprint = Blueprint("search_bp", __name__)


@search_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    search_term = request.form['search_term']
    print(type(search_term))
    if services.is_author(search_term, repo.repo_instance):
        return redirect(url_for('book_bp.books_by_author', author_name=search_term))

    elif services.is_publisher(search_term, repo.repo_instance):
        return redirect(url_for('book_bp.books_by_publisher', publisher_name=search_term))

    elif services.is_release_year(search_term, repo.repo_instance):
        return redirect(url_for('book_bp.books_by_release_year', release_year=search_term))

    elif services.is_title(search_term, repo.repo_instance):
        return redirect(url_for('book_bp.books_by_title', title=search_term))

    else:
        return render_template('nobooksfound.html')

