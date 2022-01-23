from my_web_framework import BaseController


class About(BaseController):

    def __call__(self, request):
        status_code = '200 OK'
        body = self.get_rendered_template('about.html')
        return status_code, body
