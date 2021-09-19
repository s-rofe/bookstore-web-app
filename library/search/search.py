from flask import Blueprint, redirect
from flask import render_template, url_for

import library.adapters.repository as repo
import library.search.services as services

search_blueprint = Blueprint("search_bp", __name__)


@search_blueprint.route('/search/<search_term>', methods=['GET'])
def search(search_term):
    if services.is_author(search_term):
        return redirect(url_for('book_bp.book_by_author', author_name=search_term))

    elif services.is_publisher(search_term):
        return redirect(url_for('book_bp.book_by_publisher', publisher_name=search_term))

    elif services.is_release_year(search_term):
        return redirect(url_for('book_bp.book_by_release_year', release_year=search_term))

    else:
        return render_template('nobooksfound.html')
