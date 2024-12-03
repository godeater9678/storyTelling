class CommonResponse:
    statusCode = None
    data = None

    def __init__(self, data=None, statusCode=200):
        self.data = data
        self.statusCode = statusCode
