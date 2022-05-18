class LoginCommand:
    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password = password
