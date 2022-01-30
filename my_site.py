from my_web_framework import Application
from routes import ROUTES
from controllers import MyFrontController
from model import TrainingSite
front_controllers = [
    MyFrontController
]
my_site_model = TrainingSite()
application = Application(ROUTES, front_controllers, my_site_model)
