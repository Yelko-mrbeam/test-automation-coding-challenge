from flask import render_template, Blueprint, g, abort, url_for, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__, url_prefix='/app/<string:lang_code>')


@main.url_defaults
def add_language_code(endpoint, values):
    if g.get('lang_code') is None:
        g.lang_code = 'en'
    values.setdefault('lang_code', g.lang_code)


@main.url_value_preprocessor
def pull_lang_code(endpoint, values):
    if g.get('lang_code') is None:
        g.lang_code = 'en'
    g.lang_code = values.pop('lang_code')


@main.route('/user/login.html')
def login():
    """
    Displays the login page
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.land'))
    return render_template('login_user.html')


@main.route('/user/landing.html')
@login_required
def land():
    """
    Displays the login page
    """
    return render_template('landing_page.html')


@main.route('/user/profile.html')
@login_required
def profile():
    """
    Displays the profile
    """
    return render_template('profile_user.html')


@main.route('/not_found.html')
@login_required
def four_o_four():
    """
    Displays the profile
    """
    abort(404)


@main.route('/service_unavailable.html')
@login_required
def service_unavailable():
    """
    Displays the profile
    """
    abort(503)
