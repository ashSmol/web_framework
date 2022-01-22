class NotFoundPage:
    def __call__(self):
        status_code = '404 Error'
        body = b'<h1> !Page not found. 404 Error !!!</h1>'
        return status_code, body

