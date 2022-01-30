from my_web_framework import Application
from routes import ROUTES
from controllers import MyFrontController
from model import TrainingSite
front_controllers = [
    MyFrontController
]

my_site_model = TrainingSite()
my_site_model.course_categories = ['Programming', 'Management', 'Testing']
my_site_model.courses = ['Java', 'Python', 'JS']
my_site_model.students = ['Vasya Pupkin', 'Yura Lyubkin', 'Kolya Kot']

application = Application(ROUTES, front_controllers, my_site_model)
