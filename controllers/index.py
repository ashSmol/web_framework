from my_web_framework import BaseController


class Index(BaseController):

    def __call__(self, request):
        status_code = '200 OK'
        body = self.get_rendered_template('index.html')
        return status_code, body
