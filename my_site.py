from my_web_framework import Application
from patterns import ObjectBuilder
from routes import ROUTES
from controllers import MyFrontController
from model import TrainingSite
from logger import Logger

logger = Logger('my_logger')

front_controllers = [
    MyFrontController
]

my_site_model = TrainingSite()

programming_category = ObjectBuilder('category').set_obj_name('Programming').set_obj_description(
    'programming description').build()
testing_category = ObjectBuilder('category').set_obj_name('Testing').set_obj_description(
    'testing description').build()

logger.log('creating course categories!!!')

python_course = ObjectBuilder('course').set_obj_name('Python').set_obj_description(
    'python course description').build()
java_course = ObjectBuilder('course').set_obj_name('Java').set_obj_description(
    'Java course description').build()

logger.log('creating courses!!!')


my_site_model.course_categories = [programming_category, testing_category]
my_site_model.courses = [python_course, java_course]
my_site_model.students = ['Vasya Pupkin', 'Yura Lyubkin', 'Kolya Kot']

application = Application(ROUTES, front_controllers, my_site_model)
