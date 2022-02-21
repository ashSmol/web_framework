from pprint import pprint

from my_web_framework import BaseController, Debug
from patterns import ObjectBuilder

from my_site import application


@application.url('/create_course')
class CreateCourse(BaseController):
    @Debug()
    def __call__(self, request, model):
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

            new_course = ObjectBuilder('course')
            new_course.set_obj_name(template_params['course_name'])
            new_course.set_obj_description(template_params['course_description'])
            new_course = new_course.build()
            model.add_new_course(new_course)
            template_params.update({'course': new_course})

            body = self.get_rendered_template('create_course.html', template_params)
            return status_code, body

        template_params.update({'courses': model.course_categories})
        body = self.get_rendered_template('create_course.html', template_params)

        return status_code, body
