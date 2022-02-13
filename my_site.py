import sqlite3

from my_web_framework import Application
from patterns import ObjectBuilder, CourseMapper, StudentMapper
from patterns.mappers import CourseStudentLinkMapper
from routes import ROUTES
from controllers import MyFrontController
from logger import Logger

logger = Logger('my_logger')

front_controllers = [
    MyFrontController
]


class TrainingSite:
    course_categories: list
    courses: list
    students: list

    def __init__(self, _connection):
        self.connection = _connection

    def get_categories(self):
        return self.course_categories

    def get_courses(self):
        return CourseMapper(self.connection).find_all()

    def get_course_by_id(self, course_id):
        return CourseMapper(self.connection).find_by_id(course_id)

    def sign_up_student_for_course(self, course, student):
        if not (student in course):
            CourseStudentLinkMapper(self.connection).insert(course, student)

    def find_students_for_course(self, course):
        links = CourseStudentLinkMapper(self.connection).find_students_for_course(course.id)
        result = []
        for link in links:
            result.append(self.get_student_by_id(link.student_id))
        return result

    def add_new_course(self, course):
        CourseMapper(self.connection).insert(course)

    def get_students(self):
        return StudentMapper(self.connection).find_all()

    def get_student_by_id(self, student_id):
        return StudentMapper(self.connection).find_by_id(student_id)

    def add_new_student(self, student):
        StudentMapper(self.connection).insert(student)


connection = sqlite3.Connection('my_db.db')
my_site_model = TrainingSite(connection)

programming_category = ObjectBuilder('category').set_obj_name('Programming').set_obj_description(
    'programming description').build()
testing_category = ObjectBuilder('category').set_obj_name('Testing').set_obj_description(
    'testing description').build()

logger.log('creating course categories!!!')

logger.log('creating courses!!!')

my_site_model.course_categories = [programming_category, testing_category]

application = Application(ROUTES, front_controllers, my_site_model)
