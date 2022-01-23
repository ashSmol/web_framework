from my_web_framework import Application
from routes import ROUTES
from controllers import MyFrontController
front_controllers = [
    MyFrontController
]

application = Application(ROUTES, front_controllers)
