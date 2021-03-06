from better_profanity import profanity
from flask import Blueprint
from flask import request, render_template, url_for, session, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, HiddenField
from wtforms.validators import Length, ValidationError

import library.adapters.repository as repo
import library.reviews.services as services
from library.authentication.authentication import login_required

reviews_blueprint = Blueprint("reviews_bp", __name__)


@reviews_blueprint.route('/reviews', methods=['GET'])
def reviews():
    book_id = request.args.get('book_id')
    reviews_list = services.get_reviews(int(book_id), repo.repo_instance)
    book = services.get_book_by_id(int(book_id), repo.repo_instance)
    return render_template(
        'books/reviews.html',
        title='Reviews',
        reviews_title=book.title,
        reviews=reviews_list,
        book=book
    )


@reviews_blueprint.route('/write_review', methods=['GET', 'POST'])
@login_required
def write_review():
    form = ReviewForm()
    user_name = session['user_name']

    if form.validate_on_submit():
        book_id = int(form.book_id.data)
        services.add_review(book_id, form.review.data, int(form.rating.data), user_name, repo.repo_instance)
        return redirect(url_for('reviews_bp.reviews', book_id=book_id))

    if request.method == 'GET':
        book_id = int(request.args.get('book_id'))
        form.book_id.data = book_id

    else:
        book_id = int(form.book_id.data)

    book = services.get_book_by_id(book_id, repo.repo_instance)
    return render_template(
        'books/write_review.html',
        title='Write Review',
        book=book,
        form=form
    )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Review must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class ReviewForm(FlaskForm):
    review = TextAreaField('Review', [
        Length(min=4, message='Your review is too short'),
        ProfanityFree(message='Profanity is not allowed')])
    rating = SelectField('Rating', choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'),
                                            (5, '5 Stars')])
    book_id = HiddenField("Book id")
    submit = SubmitField('Submit')
