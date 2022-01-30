from pprint import pprint

from model import TrainingSite
from my_web_framework import BaseController


class Courses(BaseController):

    def __call__(self, request, model: TrainingSite):
        status_code = '200 OK'
        template_params = {}

        print('*' * 100)
        pprint(self.get_request_method(request))
        print('*' * 100)

        if self.get_request_method(request) == 'GET':
            pprint(self.get_get_params(request))

        if self.get_request_method(request) == 'POST':
            template_params.update(self.get_post_params(request))
            print(f'template params: {template_params}')
            body = self.get_rendered_template('categories.html', template_params)
            return status_code, body

        template_params.update({'courses': model.courses})
        body = self.get_rendered_template('courses.html', template_params)

        return status_code, body