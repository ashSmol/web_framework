class About:
    def __call__(self):
        status_code = '200 OK'
        body = b'About page!'
        return status_code, body
