from flask_login import UserMixin
from utils import Singleton


class LoginManagerService(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.logged_in = None

    def load_user(self, user_identifier):
        if user_identifier == '1':
            new_user = UserMixin()
            new_user.id = 1
            new_user.name = "test"
            return new_user
        return None
