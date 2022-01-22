from my_web_framework import Application
from routes import ROUTES
from jinja2 import Environment, PackageLoader

front_controllers = [

]

application = Application(ROUTES, front_controllers)
