from pprint import pprint
from my_web_framework import BaseController


class Contact(BaseController):

    def __call__(self, request):
        status_code = '200 OK'
        body = self.get_rendered_template('contact.html')
        print('*'*100)
        pprint(request)
        print('*'*100)
        return status_code, body
