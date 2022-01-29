from pprint import pprint
from my_web_framework import BaseController


class About(BaseController):

    def __call__(self, request):
        status_code = '200 OK'
        template_params = {}
        body = self.get_rendered_template('about.html', template_params)
        print('Hello from about controller')
        pprint(request)
        return status_code, body
