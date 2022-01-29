from pprint import pprint
from my_web_framework import BaseController


class Contact(BaseController):

    def __call__(self, request):
        status_code = '200 OK'
        body = self.get_rendered_template('contact.html')
        print('*' * 100)
        pprint(self.get_request_method(request))
        print('*' * 100)

        if self.get_request_method(request) == 'GET':
            pprint(self.get_get_params(request))

        if self.get_request_method(request) == 'POST':
            pprint(self.get_post_params(request))

        return status_code, body
