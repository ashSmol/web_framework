from pprint import pprint

from my_web_framework import BaseController, Debug


class CoursePage(BaseController):
    @Debug()
    def __call__(self, request, model):
        status_code = '200 OK'
        template_params = {}

        print('*' * 100)
        pprint(self.get_request_method(request))
        print('*' * 100)
        if self.get_request_method(request) == 'GET':
            rq_params = self.get_get_params(request)
            pprint(rq_params)
            course_id = rq_params['course_id']
            if rq_params.get('action') == 'graduate':
                model.graduate_all_students_from_course(course_id)

            course_obj = model.get_course_by_id(course_id)
            course_obj.students = model.find_students_for_course(course_obj)
            template_params['course'] = course_obj
            template_params['students'] = model.get_students()

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
            course_id = rq_params['course_id']
            course_obj = model.get_course_by_id(course_id)

            student_id = rq_params['student_id']

            student_obj = model.get_student_by_id(student_id)

            model.sign_up_student_for_course(course_obj, student_obj)

            print(f'DEBUGGGG course: {course_obj}\n student: {student_obj} ')
            template_params['course'] = course_obj
            template_params['students'] = model.get_students()
            print(f'template params: {template_params}')
            body = self.get_rendered_template('course.html', template_params)
            return status_code, body

        template_params.update({'course': model.courses})
        body = self.get_rendered_template('course.html', template_params)

        return status_code, body
