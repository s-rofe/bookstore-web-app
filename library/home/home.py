from flask import Blueprint
from flask import request, render_template, url_for

import library.adapters.repository as repo
import library.book.services as services

home_blueprint = Blueprint("home_bp", __name__)


@home_blueprint.route('/')
def home():
    return render_template('home/home.html')