from my_web_framework import Application
from patterns import ObjectBuilder
from routes import ROUTES
from controllers import MyFrontController
from model import TrainingSite

front_controllers = [
    MyFrontController
]

my_site_model = TrainingSite()

programming_category = ObjectBuilder('category').set_obj_name('Programming').set_obj_description(
    'programming description').build()
testing_category = ObjectBuilder('category').set_obj_name('Testing').set_obj_description(
    'testing description').build()

my_site_model.course_categories = [programming_category, testing_category]
my_site_model.courses = ['Java', 'Python', 'JS']
my_site_model.students = ['Vasya Pupkin', 'Yura Lyubkin', 'Kolya Kot']

application = Application(ROUTES, front_controllers, my_site_model)
