class MyFrontController:
    def __init__(self, request: dict):
        self.request = request

    def __call__(self):
        self.request.update({'some_key': 'some_value'})
        return self.request
