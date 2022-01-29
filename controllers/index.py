from my_web_framework import BaseController


class Index(BaseController):

    def __call__(self, request):
        status_code = '200 OK'
        template_params = {}
        body = self.get_rendered_template('index.html', template_params)
        return status_code, body
