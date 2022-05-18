import logging

from flask import Blueprint, jsonify, flash, request, abort
from flask_login import login_required, logout_user, current_user, login_user, UserMixin

from command import LoginCommand
from utils import CommandUtils

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login/user', methods=['POST'])
def login():
    command = CommandUtils.get_command_from_json_data(request, LoginCommand)
    if command.username == "test" and command.password == "test":
        new_user = UserMixin()
        new_user.id = 1
        new_user.name = command.username
        login_user(new_user)
        flash('User logged in')
        logging.debug('User logged in')
        return 'ok'

    abort(400)


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    current_user.authenticated = False
    logout_user()
    return jsonify('ok')
