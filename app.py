import logging
import os

from flask import Flask

from extensions import login_manager
from rest_handler.authentication_handler import auth
from rest_handler.root_handler import root
from rest_handler.template_handler import main
from service import LoginManagerService


def create_app() -> Flask:
    os.environ["TZ"] = "UTC"
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.register_blueprint(root)
    app.register_blueprint(auth)
    app.register_blueprint(main)

    init_extensions(app)

    return app


def init_extensions(app):
    login_manager.init_app(app)
    logging.basicConfig(level=logging.DEBUG)


@login_manager.user_loader
def load_user(user_id):
    return LoginManagerService().load_user(user_id)
