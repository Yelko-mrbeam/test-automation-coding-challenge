from flask import redirect, url_for, Blueprint, g

root = Blueprint('root', __name__, url_prefix='/')


@root.route("/")
def entry_url():
    return redirect(url_for('main.login'))
