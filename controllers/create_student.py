from pprint import pprint

from model import TrainingSite, Student
from my_web_framework import BaseController, Debug
from patterns import ObjectBuilder


class CreateStudent(BaseController):
    @Debug()
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

            new_student = Student(template_params['firstname'], template_params['surname'])
            model.students.append(new_student)
            template_params.update({'student': new_student})

            body = self.get_rendered_template('create_student.html', template_params)
            return status_code, body

        template_params.update({'students': model.students})
        body = self.get_rendered_template('create_student.html', template_params)

        return status_code, body
