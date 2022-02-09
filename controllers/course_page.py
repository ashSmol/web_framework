from pprint import pprint

from model import TrainingSite, Course
from my_web_framework import BaseController, Debug


class CoursePage(BaseController):
    @Debug()
    def __call__(self, request, model: TrainingSite):
        status_code = '200 OK'
        template_params = {}

        print('*' * 100)
        pprint(self.get_request_method(request))
        print('*' * 100)
        if self.get_request_method(request) == 'GET':
            rq_params = self.get_get_params(request)
            course_name = rq_params['name']
            course_obj = model.get_course_by_name(course_name)
            template_params['course'] = course_obj
            template_params['students'] = model.students

            pprint(template_params)
            print(course_obj.name)
            for student in course_obj:
                print('----')
                print(student.name)
                print(student.surname)
                print('----')

            body = self.get_rendered_template('course.html', template_params)
            return status_code, body

        if self.get_request_method(request) == 'POST':
            rq_params = self.get_post_params(request)
            course_name = rq_params['course_name']
            course_obj = model.get_course_by_name(course_name)

            student = rq_params['student'].split('+')

            student_obj = model.get_student(student[0], student[1])

            course_obj.add_student(student_obj)
            template_params['course'] = course_obj
            template_params['students'] = model.students
            print(f'template params: {template_params}')
            body = self.get_rendered_template('course.html', template_params)
            return status_code, body

        template_params.update({'course': model.courses})
        body = self.get_rendered_template('course.html', template_params)

        return status_code, body
