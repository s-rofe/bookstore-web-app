from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

import library.adapters.repository as repo
import library.book.services as services

book_blueprint = Blueprint("book_bp", __name__)


@book_blueprint.route('/browse_books', methods=['GET'])
def browse_books():
    pass
