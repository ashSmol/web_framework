import time
from pprint import pprint

from my_site import application
from my_web_framework import BaseController
from my_web_framework import Debug

print('before declared class')


@application.url('/about')
class About(BaseController):
    @Debug()
    def __call__(self, request, model):
        status_code = '200 OK'
        template_params = {}
        body = self.get_rendered_template('about.html', template_params)
        print('Hello from about controller')
        time.sleep(1)
        return status_code, body
