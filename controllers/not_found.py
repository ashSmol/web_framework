class NotFoundPage:
    def __call__(self):
        status_code = '404 Error'
        body = b'Page not found. 404 Error'
        return status_code, body