from flask import Request


class CommandUtils:
    @staticmethod
    def get_command_from_json_data(request: Request, constructor: type) -> type:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.get_json(silent=True)
            if json is None:
                return None
            else:
                return constructor(**json)
        else:
            raise Exception()