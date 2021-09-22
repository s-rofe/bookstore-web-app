from flask import Blueprint, render_template, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from password_validator import PasswordValidator
import library.authentication.services as services
import library.adapters.repository as repo
from functools import wraps

authentication_blueprint = Blueprint('authentication_bp', __name__, url_prefix='/authentication')

stored_url = None


@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    error_message = None

    if form.validate_on_submit():
        # if username and password is POST'ed try to add the new user
        try:
            services.add_user(form.user_name.data, form.password.data, repo.repo_instance)
            # Once registered take the user to the login page
            return redirect(url_for('authentication_bp.login'))
        except services.NameNotUniqueException:
            error_message = 'Username taken - please try another'

    # For get or failed POST
    return render_template(
        'authentication/credentials.html',
        title='Register',
        form=form,
        user_name_error_message=error_message,
        handler_url=url_for('authentication_bp.register')
    )


@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username_not_found = None
    password_doesnt_match = None
    referrer = request.headers.get('Referer')

    if form.validate_on_submit():
        # Look up the user in the repo
        try:
            user = services.get_user(form.user_name.data, repo.repo_instance)
            # Check password and user match
            services.authenticate_user(user.user_name, form.password.data, repo.repo_instance)

            session.clear()
            # Create session then take the user to the home page
            session['user_name'] = user.user_name
            referrer = request.headers.get('Referer')
            return redirect(services.get_stored_url(repo.repo_instance))

        except services.UnknownUserException:
            username_not_found = 'User not found - please try again'

        except services.AuthenticationException:
            password_doesnt_match = 'Password doesnt match Username - please try again'

        # For GET or failed POST
    if request.method == 'GET':
        services.set_stored_url(referrer, repo.repo_instance)
    return render_template(
        'authentication/credentials.html',
        title='Login',
        user_name_error_message=username_not_found,
        password_error_message=password_doesnt_match,
        form=form,
    )


@authentication_blueprint.route('/logout')
def logout():
    # Clear the session and take the user to the home page
    session.clear()
    return redirect(url_for('home_bp.home'))


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_name' not in session:
            return redirect(url_for('authentication_bp.login'))
        return view(**kwargs)

    return wrapped_view


class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = 'Password must be at least 8 characters long and contain upper case and lower case letters, ' \
                      'and a digit '
            self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema.min(8)
        schema.has().lowercase()
        schema.has().uppercase()
        schema.has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    user_name = StringField('Username', [
        DataRequired(message='Username is required'),
        Length(min=4, message='Username too short')])
    password = PasswordField('Password', [
        DataRequired(message='Password required'),
        PasswordValid()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    user_name = StringField('Username', [
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired()])
    submit = SubmitField('Login')
