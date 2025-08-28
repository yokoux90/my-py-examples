


class QueryException(Exception):
    code: str
    message: str

    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message